#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        if len(line) > 2:
            line = line.strip()
            c_line = line[0].capitalize()
            last_c =line[-1].capitalize()
            print(c_line + line[1:-1] + last_c)

if __name__ == '__main__':
    main()