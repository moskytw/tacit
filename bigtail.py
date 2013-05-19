#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__version__ = '0.1'

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

    fragment = None

    while True:

        # read the chunk form file
        chunk = f.read(buffer_size)
        if not chunk:
            if fragment:
                yield fragment
            break

        # handle the chunk
        lines = chunk.splitlines(True)

        if fragment:
            if lines[-1].endswith('\n'):
                yield fragment
            else:
                yield lines.pop(-1)+fragment
            fragment = ''

        if lines:
            fragment = lines.pop(0)

        for line in reversed(lines):
            yield line

        # prepare for next reading
        step_size = -buffer_size*2 # include the range it read
        if f.tell()+step_size >= 0:
            f.seek(step_size, os.SEEK_CUR)
        else:
            # read the final chunk
            buffer_size = f.tell()-buffer_size
            f.seek(0)

if __name__ == '__main__':

    import sys

    path = 'data/access.log'
    if len(sys.argv) == 2:
        path = sys.argv[1]

    for line in tail(path):
        print line,
