#!/usr/bin/env python3

import sys

def matches(w, evil_str):
    return [c for c in w if c in evil_str] == list(evil_str)

def main():
    words = [line.strip() for line in sys.stdin]
    evil_words = [w for w in words if (matches(w.lower(), "evil"))]
    for w in evil_words:
        print(w)

if __name__ == '__main__':
    main()
