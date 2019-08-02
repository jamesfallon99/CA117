#!/usr/bin/env python3

import sys

def conv(n, base):
    return int(str(n), base)

def main():
    for l in sys.stdin:
        print(conv(*[int(n) for n in l.split()]))

if __name__ == '__main__':
	main()
