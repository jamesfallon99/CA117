#!/usr/bin/env python3

import sys

def cam(s):
    return " ".join([f.capitalize() for f in s.split()])

def main():
    for line in sys.stdin:
        print(cam(line))

if __name__ == "__main__":
    main()
