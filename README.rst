Big Tail
========

It provides an useful function, ``tail``, which lets you read lines in a file
from the end. It works like the ``tac`` command in the shell.

It reads file into a fixed buffer and yields lines orderly, so it is comportable
to use on big file. (ex. large log)

Installation
------------

You can install it via PyPI,

::

    sudo pip install bigtail

or download it manually.

An Example
----------

The content of file:

::

    The first line.
    The second line.
    The last line.

The code:

::

    for line in open(path):
        print line,
    print

    from bigtail import tail

    for line in tail(path):
        print line,

The output:

::

    The first line.
    The second line.
    The last line.

    The last line.
    The second line.
    The first line.
