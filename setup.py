from distutils.core import setup

setup(
    name='imagefacts',
    version='1.0',
    description="Find out the screen dimensions of the commonest image formats from a URL or bytestring",
    author='Mark Paschal',
    author_email='markpasc@markpasc.org',
    url='https://github.com/markpasc/imagefacts',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=['imagefacts'],
)
