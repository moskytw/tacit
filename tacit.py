#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2.1'

import os

def tac_slices(file_or_path, buffer_size=None):

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

        # move to the start of next slice
        if f.tell()-buffer_size > 0:
            f.seek(-buffer_size, os.SEEK_CUR)
        else:
            buffer_size = f.tell()
            f.seek(0)

        slice = f.read(buffer_size)
        if not slice: break

        # restore the pointer after reading the file
        f.seek(-buffer_size, os.SEEK_CUR)

        yield slice

    if open_by_me:
        f.close()

def tac(file_or_path, buffer_size=None):
    
    segment = ''

    for slice in tac_slices(file_or_path, buffer_size):

        lines = slice.splitlines(True)

        # check the integrity of the segment
        if segment and lines[-1].endswith('\n'):
            # segment is a complete line, because the last line ends with '\n'
            yield segment
            segment = ''

        # the last line of this slice may be a part of previous segment
        segment = lines.pop(-1)+segment

        if lines:

            # the segment is a complete line, because there has other '\n'
            yield segment

            # the first line may be a segment
            segment = lines[0]

            for line in reversed(lines[1:]):
                yield line

    if segment:
        yield segment
