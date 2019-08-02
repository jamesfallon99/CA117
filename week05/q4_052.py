#!/usr/bin/env python3

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
            d[food] = int(tokens[-1])

    for line in sys.stdin:
        line = line.strip().split(",")
        name = line[0]
        foodstuff = line[1:]
        calories = 0
        for word in foodstuff:
            if word in d:
                calories += d[word]
            else:
                calories += 100
            people[name] = calories

    for t in sorted(people.items(), key=sorter):
        print('{:>{}s} : {:>{}d}'.format(t[0], len(max(people.keys(), key=len)), t[1], len(str(max(people.values())))))

if __name__ == '__main__':
    main()
