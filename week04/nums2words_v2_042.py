#!/usr/bin/env python3

import sys
def main():
    d = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
    }
    for line in sys.stdin:
        tokens = line.strip().split()
        lis = []
        for num in tokens:
            if num in d:
                lis.append(d[num])
            else:
                lis.append("unknown")
        print(" ".join(lis))

if __name__ == '__main__':
    main()
