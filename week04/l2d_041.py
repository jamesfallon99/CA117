#!/usr/bin/env python3

import sys

def l2d(filename):
    d = {}
    key = filename.readline().strip().split()
    value = filename.readline().strip().split()
    i = 0
    while i < len(key):
        d[key[i]] = value[i]
        i += 1

    return d
