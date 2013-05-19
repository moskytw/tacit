#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bigtail import tail_chunks

for chunk in tail_chunks('data/ordered.list', 2):
    print repr(chunk)
