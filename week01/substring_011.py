#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        if words[0].lower() in words[1].lower():
            print(True)
        else:
            print(False)
        

if __name__ == '__main__':
    main()