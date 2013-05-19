#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import izip_longest
from bigtail import tail

excepted_lines = ['9\n', '8\n', '7\n', '6\n', '5\n', '4\n', '3\n', '2\n', '1\n', '0.1\n', '0.01\n']

for i in range(10):

    print 'i = ', i

    for excepted_line, line in izip_longest(excepted_lines, tail('data/ordered.list', i)):

        if i > 0 and excepted_line != line:
            print >> sys.stderr, 'Warning: i=%d, except %r, but got %r' % (i, excepted_line, line)

        print line,
    
    print

#for line in tail('data/ordered.list', 1):
#    print line,
