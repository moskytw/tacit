#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import timeit
from tacit import tac

def test():
    for line in tac('data/ordered.list'):
        line

if __name__ == '__main__':
    print timeit(test, number=100000)
