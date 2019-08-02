#!/usr/bin/env python3

import sys

def cam(s):
    return " ".join([s[0:-1] + s[-1].upper() for s in s.split()])

def main():
    for line in sys.stdin:
        print(cam(line))

if __name__ == "__main__":
    main()
