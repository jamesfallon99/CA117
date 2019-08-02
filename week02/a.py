#!/usr/bin/env python3

import sys

def anagram(chars, s):
    if len(s) == len(chars):
        for c in chars:
            if c in s:
                s = s.replace(c, "", 1)
            else:
                return False
        return True
    return False
def main():
    for line in sys.stdin:
        [chars, s] = line.lower().strip().split()
        print(anagram(chars, s))

if __name__ == '__main__':
    main()
