#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    sl = list(s)
    for i in range(1, len(s), 2):
        sl[i - 1], sl[i] = sl[i], sl[i - 1]
    print("".join(sl))

if __name__ == '__main__':
    main()
