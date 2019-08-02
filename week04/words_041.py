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
    for k, v in sorted(d.items()):
        print("{} : {}".format(k, v))


if __name__ == '__main__':
    main()
