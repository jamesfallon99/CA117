#!/usr/bin/env python3

import sys

def main():
    total = 0
    for line in sys.stdin:
        tokens = line.strip().split()
        i = 0
        while i < len(tokens):
            total = total + 1
            i = i + 1
    print(total)


if __name__ == '__main__':
    main()
