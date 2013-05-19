Big Tail
========

It provides an useful function, ``tail``, which lets you read file from the end.
It is useful for parsing log file.

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
