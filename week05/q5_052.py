#!/usr/bin/env python3

import sys

def sorter(t):
    return t[1]

def main():
    d = {}
    skipped = []
    total = 0

    for line in sys.stdin:
        tokens = line.strip().split(":")
        nums = tokens[1].split(",")
        total = 0

        try:
            for n in nums:
                total += int(n)
        except ValueError:
            skipped.append(tokens[0])
        else:
            d[tokens[0]] = total

    for k, v in sorted(d.items(), key=sorter, reverse=True):
        print("{} : {}".format(k, v))

    print("Skipped:")

    for student in skipped:
        print(student)

if __name__ == '__main__':
    main()
