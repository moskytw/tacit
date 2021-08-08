Tacit
=====

It provides the useful function, ``tac``, which lets you read lines from end of
file. It works like the ``tac`` command in the shell.

It reads file into a fixed buffer and yields lines orderly, so it is comportable
to use on big file, e.g., large log.

Examples
--------

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

    from tacit import tac

    for line in tac(path):
        print line,

The output:

::

    The first line.
    The second line.
    The last line.

    The last line.
    The second line.
    The first line.

There are more examples: `/examples
<https://github.com/moskytw/tacit/tree/dev/examples>`_.
