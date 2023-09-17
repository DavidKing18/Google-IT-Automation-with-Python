#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.title() for word in words]))

