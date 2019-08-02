#!/usr/bin/env python3

import sys

def revcom(words):
    true = {word.lower():True for word in words if len(word) >= 5}
    words = [word for word in words if word.lower()[::-1] in true]
    return words

def main():
    words = [word.strip() for word in sys.stdin]
    print(revcom(words))

if __name__ == '__main__':
    main()