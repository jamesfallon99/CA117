#!/usr/bin/env python3

import sys

def qnou(l):
    return "q" in l and l.count("q") > l.count("qu")

def main():
    lines = [l.strip() for l in sys.stdin]

    print("Words with q but no u: {}".format(qnou(lines)))
if __name__ == '__main__':
    main()
