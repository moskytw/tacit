#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tacit import tac

for line in tac('data/access.log'):
    print line,
