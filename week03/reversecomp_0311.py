#!/usr/bin/env python3

import sys

def revcom(words):
    return([word for word in words if len(word) >= 5 and word[::-1] in words])

def main():
    words = [word.strip() for word in sys.stdin]
    print(revcom(words))

if __name__ == '__main__':
    main()
