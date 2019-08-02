#!/usr/bin/env python3

import sys

def matches(w, aeiou_str):
    return[c for c in w if c in aeiou_str] == list(aeiou_str)

def main():
    lines = [line.strip() for line in sys.stdin]
    aeiou = [w for w in lines if matches(w.lower(), "aeiou")]
    for w in aeiou:
        print(w)

if __name__ == '__main__':
    main()
