#!/usr/bin/env python3

import sys

def build_dictionary(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()
            d[tokens[0]] = int(tokens[1])
    return d

def extract_range(d, low, high):
    nd = {}
    for i in d:
        if low <= d[i] <= high:
            nd[i] = d[i]
    return nd
