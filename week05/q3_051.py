#!/usr/bin/env python3

import sys

def transform(c):
    if c.isupper():
        return c
    return "0"

def main():
    for lines in sys.stdin:
        line = lines.strip()
        uppers = ("".join([transform(c) for c in line.strip()]))
        upper_tokens = uppers.split("0")
        print(max(upper_tokens, key=len))


if __name__ == '__main__':
    main()
