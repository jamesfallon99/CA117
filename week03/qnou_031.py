#!/usr/bin/env python3

import sys

def qnotu(l):
    return "q" in l and l.count("q") > l.count("qu")

def main():
    words = []

    for line in sys.stdin:
        words.append(line.strip())

    print("Words with q but no u: {}".format([word for word in words if qnotu(word.lower())]))

if __name__ == '__main__':
    main()
