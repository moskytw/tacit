#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from bigtail import tail

if len(sys.argv) != 2:
    print >> sys.stderr, 'Give me a path.'
    sys.exit(1)

for line in tail(sys.argv[1]):
    print line,
