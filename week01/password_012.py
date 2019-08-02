#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        digit = False
        lower = False
        upper = False
        special = False
        for c in line:
            if c.isdigit():
                digit = c.isdigit()
            elif c.islower():
                lower = c.islower()
            elif c.isupper():
                upper = c.isupper()
            else:
                special = not c.isdigit() and not c.islower() and not c.isupper()
        total = 0
        print(digit + lower + upper + special)

if __name__ == '__main__':
    main()
