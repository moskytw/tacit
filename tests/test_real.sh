#!/bin/bash

python tests/test_real.py > r1
tac data/access.log > r2
vimdiff r{1,2}
rm r{1,2}
