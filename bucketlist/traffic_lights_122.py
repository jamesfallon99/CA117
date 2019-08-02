#!/usr/bin/env python3

import sys

def main():
    wait = 0
    s = int(sys.stdin.readline().strip())
    for line in sys.stdin:
        tokens = line.split()
        d = int(tokens[0])
        r = int(tokens[1])
        g = int(tokens[2])

        mod = (d + wait) % (r + g)
        if mod < r:
            wait = wait + (r - mod)

    print(s + wait)


if __name__ == '__main__':
    main()
