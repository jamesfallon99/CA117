#!/usr/bin/env python3

import sys

def main():
    d = {}
    file = sys.argv[1]
    with open(file, "r") as f:
        for line in f:
            name, phone = line.strip().split()
            d[name] = phone
    for name in sys.stdin:
        name = name.strip()
        print("Name: {}".format(name))
        try:
            print("Phone: {}".format(d[name]))
        except KeyError:
            print("No such contact")

if __name__ == '__main__':
    main()
