#!/usr/bin/env python3

import sys
import string
def make_dictionary():
    d = {}
    for line in sys.stdin:
        for w in line.lower().split():
            w = w.strip(string.punctuation)
            if not w:
                continue
            try:
                d[w] += 1
            except KeyError:
                d[w] = 1
    return d

def main():
    d = make_dictionary()
    nd = {}
    for k, v in sorted(d.items()):
        if len(k) > 3 and int(v) >= 3:
            nd[k] = v
    max_key_width = len(max(nd.keys(), key=len))
    for k, v in sorted(nd.items()):
        print("{:>{:d}} : {:>2d}".format(k, int(max_key_width), v))

if __name__ == '__main__':
    main()
