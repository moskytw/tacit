from distutils.core import setup

from bigtail import __version__

setup(
    name    = 'bigtail',
    description = 'It provides an useful function which lets you read lines from the end.',
    long_description = open('README.rst').read(),
    version = __version__,
    author  = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    #url = 'http://bigtail.mosky.tw/',
    py_modules = ['bigtail'],
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

