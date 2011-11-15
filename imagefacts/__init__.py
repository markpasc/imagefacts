import httplib
import urlparse

import imagefacts.open_resource
import imagefacts.getimageinfo
from imagefacts.getimageinfo import HeaderError, UnidentifiedHeaderError, InsufficientHeaderError


__version__ = '1.1'

USER_AGENT = '{0}/{1}'.format(__name__, __version__)

GET_BYTES = 10240


def _handle_url(url):
    urlparts = urlparse.urlsplit(url)
    conn_class = httplib.HTTPSConnection if urlparts.scheme == 'https' else httplib.HTTPConnection
    http = conn_class(urlparts.netloc, timeout=10)
    http.request('GET', url, headers={
        'Range': 'bytes=0-{0}'.format(GET_BYTES - 1),
        'User-Agent': USER_AGENT,
    })
    resp = http.getresponse()
    resp_bytes = resp.read(GET_BYTES)
    resp.close()  # fy, gm
    return imagefacts.open_resource._StringIO(resp_bytes)


def facts(url_file_stream_or_string):
    """Determine the type, width, and height for the specified image.

    If the parameter is a byte string, the image data it contains is examined.
    If the parameter is a file or file-like object, it is read to test the
    image data it contains.

    If the parameter is a URL, it is fetched for up to 10k of data, which is
    interpreted as the image data. The declared `Content-Type` with which the
    resource is served is not used to determine the image type, only the
    response body.

    If the image data is not a known image type, an `UnidentifiedHeaderError`
    is raised. The known types are ``image/gif``, ``image/png``, and
    ``image/jpeg``.

    If not enough of the header is present to determine the image's
    dimensions, an `InsufficientHeaderError` exception is raised. (This should
    generally only happen when examining an ``image/jpeg`` image by URL, as
    JPEG headers can in some cases exceed 10 kilobytes.)

    The image's information is returned as a tuple of the type, width, and
    height respectively.

    """
    source = imagefacts.open_resource._open_resource(url_file_stream_or_string, _handle_url)
    data = source.read()
    return imagefacts.getimageinfo.getImageInfo(data)
