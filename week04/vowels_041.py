#!/usr/bin/env python3

import sys
import string
def make_dictionary():
    d = {}
    vowels = "aeiou"
    for line in sys.stdin:
        for w in line.lower().split():
            w = w.strip(string.punctuation)
            for l in w:
                for c in vowels:
                    if c == l:
                        try:
                            d[c] += 1
                        except KeyError:
                            d[c] = 1
    return d

def sort_on_second(t):
    return t[1]

def main():
    d = make_dictionary()
    max_value_width = len(str(max(d.values())))
    for k, v in sorted(d.items(), key=sort_on_second, reverse=True):
        print("{:s} : {:>{}d}".format(k, v, max_value_width))

if __name__ == '__main__':
    main()
