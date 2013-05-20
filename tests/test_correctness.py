#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import izip

from tacit import tac

ordered_list_path = 'data/ordered.list'

expected_lines = open(ordered_list_path).read().splitlines(True)
expected_lines.reverse()

expected_count = len(expected_lines)

for bsize in range(10):

    count = 0

    for expected_line, line in izip(
        expected_lines,
        tac(ordered_list_path, bsize)
    ):
        if line != expected_line:
            print >> sys.stderr, 'error: bsize=%d, expected_line=%r, line=%r' % (bsize, expected_line, line)
        count += 1

    if bsize > 0:
        if count != expected_count:
            print >> sys.stderr, 'error: bsize=%d, expected_count=%r, count=%r' % (bsize, expected_count, count)
    else:
        if count != 0:
            print >> sys.stderr, 'error: bsize=%d, expected_count=0, count=%r' % (bsize, count)
