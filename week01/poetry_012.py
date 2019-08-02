#!/usr/bin/env python3

import sys

def main():
    largest = 0
    poem = []
    for line in sys.stdin:
        line = line.strip()
        poem.append(line)
        if len(line) > largest:
            largest = len(line)

    for line in poem:
        print('{:^{}}'.format(line, largest))

if __name__ == '__main__':
    main()
