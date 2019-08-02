#!/usr/bin/env python3

import sys

def main():
    d = {}
    file = sys.argv[1]
    with open(file, "r") as f:
        for line in f:
            name, phone, email = line.strip().split()
            d[name] = phone, email
    for name in sys.stdin:
        name = name.strip()
        print("Name: {}".format(name))
        try:
            print("Phone: {}".format(d[name][0]))
            print("Email: {}".format(d[name][1]))
        except KeyError:
            print("No such contact")

if __name__ == '__main__':
    main()
