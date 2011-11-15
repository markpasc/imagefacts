==========
imagefacts
==========

imagefacts discovers the screen dimensions of the commonest image formats from
a URL or a bytestring.


Installation
============

Install the latest imagefacts from PyPI::

   $ pip install imagefacts
   # or
   $ easy_install imagefacts


Usage
=====

Use the `imagefacts.facts()` function to find an image's dimensions::

   >>> import imagefacts
   >>> imagefacts.facts(open('localfile.jpg').read())  # byte string
   ('image/jpeg', 1024, 768)
   >>> imagefacts.facts(open('localfile.jpg'))  # file object
   ('image/jpeg', 1024, 768)
   >>> imagefacts.facts('localfile.jpg')  # file name
   ('image/jpeg', 1024, 768)
   >>> imagefacts.facts('http://example.com/image')  # URL
   ('image/png', 400, 476)
   >>>

You can also use imagefacts from the command line::

   $ python -m imagefacts http://example.com/image
   ('image/png', 400, 476)
   $


Contributors
============

Portions of imagefacts are from the feedparser project by Mark Pilgrim and
bfg-pages by zutesmog. Thanks!
