#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bigtail import tail

for line in tail('data/access.log'):
    print line,
