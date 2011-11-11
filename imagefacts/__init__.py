import httplib
import urlparse

import imagefacts.open_resource
import imagefacts.getimageinfo


__version__ = '1.0'

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
    source = imagefacts.open_resource._open_resource(url_file_stream_or_string, _handle_url)
    data = source.read()
    return imagefacts.getimageinfo.getImageInfo(data)
