#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tacit import tac_slices

for chunk in tac_slices('data/ordered.list', 2):
    print repr(chunk)
