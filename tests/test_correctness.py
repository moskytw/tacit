#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bigtail import tail

for i in range(10):
    print 'i = ', i
    for line in tail('data/ordered.list', i):
        print line,
    print

#for line in tail('data/ordered.list', 1):
#    print line,
