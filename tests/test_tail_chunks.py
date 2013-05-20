#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tacit import tac_chunks

for chunk in tac_chunks('data/ordered.list', 2):
    print repr(chunk)
