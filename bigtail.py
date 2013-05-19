#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1.2'

import os

def tail_chunks(file_or_path, buffer_size=None):

    if buffer_size is None:
        # `buffer_size` is not a constant.
        buffer_size = 4096 # 4 kB

    open_by_me = None

    if isinstance(file_or_path, basestring):
        f = open(file_or_path)
        f.seek(0, os.SEEK_END)
        open_by_me = True
    else:
        f = file_or_path
        open_by_me = False

    while True:

        # move to the start of next chunk
        if f.tell()-buffer_size > 0:
            f.seek(-buffer_size, os.SEEK_CUR)
        else:
            buffer_size = f.tell()
            f.seek(0)

        # read the chunk form file
        chunk = f.read(buffer_size)
        if not chunk: break

        # restore the pointer after reading the file
        f.seek(-buffer_size, os.SEEK_CUR)

        yield chunk

    if open_by_me:
        f.close()

def tail(file_or_path, buffer_size=None):
    
    fragment = ''

    for chunk in tail_chunks(file_or_path, buffer_size):

        # parse the chunk
        lines = chunk.splitlines(True)

        # if the existent fragment is a complete line
        #
        # normal case:
        #     fragment : 'world.\n'
        #     lines[-1]: 'hello, '
        #
        # edge case:
        #     fragment : 'hello, world.\n'
        #     lines[-1]: 'another line.\n'
        #
        if fragment and lines[-1].endswith('\n'):
            yield fragment
            fragment = ''

        # integrate the fragments
        #
        # normal case:
        #     fragment: ['world\n']
        #     lines   : ['another line.\n', 'hello, ']
        #
        # note: the fragment integrated will be yield in next section
        #
        # edge case:
        #     lines in 1st iteration: ['ab']
        #     lines in 2nd iteration: ['cd']
        #     lines in 3rd iteration: ['e\n']
        #
        fragment = lines.pop(-1)+fragment

        # if there remains any \n, the fragment is a complete line
        if lines:

            yield fragment
            # always treat the first line as a fragment
            fragment = lines[0]

            # other lines
            for line in reversed(lines[1:]):
                yield line

    if fragment:
        yield fragment
