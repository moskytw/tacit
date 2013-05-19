#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'

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

        lines = chunk.splitlines(True)

        # handle the previous fragment
        if fragment and lines[-1].endswith('\n'):
            # fragment is complete line now
            yield fragment
            fragment = ''

        # the last line of this chunk is part of previous fragment
        fragment = lines.pop(-1)+fragment

        if lines:

            # the fragment is complete line now, because there still has '\n'
            yield fragment

            # the first line may be a fragment
            fragment = lines[0]

            for line in reversed(lines[1:]):
                yield line

    if fragment:
        yield fragment
