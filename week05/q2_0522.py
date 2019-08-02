#!/usr/bin/env python3

import sys

def main():
    vowels = ["a", "e", "i", "o", "u"]
    lines = [line.strip() for line in sys.stdin]
    for w in lines:
        lis = []
        for c in w:
            if c.lower() in vowels:
                lis.append(c.lower())
        if lis == vowels:
            print(w)

if __name__ == '__main__':
    main()
