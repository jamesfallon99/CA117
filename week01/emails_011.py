#!/usr/bin/env python3

import sys

def email(name):
    name = name.split(".")
    first = name[0].capitalize()
    second = name[1].capitalize()
    s = " ".join(name)
    s = s.strip("0123456789")
    return s.title()

def main():
    for line in sys.stdin:
        [name, mail] = line.strip().split("@")
        print(email(name))


if __name__ == '__main__':
    main()
