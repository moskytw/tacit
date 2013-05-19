#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__version__ = '0.1.1'

def tail(file_or_path, buffer_size=None):
    
    if buffer_size is None:
        # `buffer_size` is not a constant.
        buffer_size = 4096 # 4 kB

    if isinstance(file_or_path, basestring):
        f = open(file_or_path)
    else:
        f = file_or_path

    # move to the end and prepare for first reading
    f.seek(0, os.SEEK_END)
    if f.tell()-buffer_size >= 0:
        f.seek(-buffer_size, os.SEEK_END)
    else:
        buffer_size = f.tell()
        f.seek(0)

    fragment = ''

    while True:

        # read the chunk form file
        chunk = f.read(buffer_size)
        if not chunk:
            break

        lines = chunk.splitlines(True)

        if fragment and lines[-1].endswith('\n'):
            print

        fragment = lines.pop(-1)
        print 'f', repr(fragment)

        if lines[1:]:
            print
            print repr(lines[1:])

        if lines:
            print
            print 'e', repr(lines[0])

        # prepare for next reading
        step_size = -buffer_size*2 # include the range it read
        if f.tell()+step_size >= 0:
            f.seek(step_size, os.SEEK_CUR)
        else:
            # read the final chunk
            buffer_size = f.tell()-buffer_size
            f.seek(0)

    yield None
