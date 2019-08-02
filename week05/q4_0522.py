#!/usr/bin/env python

import sys

def sorter(t):
    return t[1]

def main():
    filename = sys.argv[1]
    d = {}
    people = {}
    with open(filename, "r") as f:
        for line in f:
            tokens = line.strip().split()
            food = " ".join(tokens[:-1])
            d[food] = tokens[-1]

    for line in sys.stdin:
        tokens = line.strip().split(",")
        name = tokens[0]
        foodstuff = tokens[1:]
        calories = 0
        for food in foodstuff:
            if food in d:
                calories += int(d[food])
            else:
                calories += 100
            people[name] = calories
        longest = len(max(people.keys()))
        largest = len(str(max(people.values())))
    for k, v in sorted(people.items(),key=sorter):
        print("{:>{}s} : {:>{}d}".format(k, longest, v, largest))


if __name__ == '__main__':
        main()
