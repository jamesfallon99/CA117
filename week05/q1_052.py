#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    n = int(sys.argv[2])
    n = n % len(s)
    s = s[-n:] + s[0:-n]
    print(s)

if __name__ == '__main__':
    main()
