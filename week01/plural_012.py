#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        vowels = ["a", "e", "i", "o", "u"]
        if line[-2:]  == "ch" or line[-2:] == "sh":
            line = line + "es"
        elif line[-1] == "x" or line[-1] == "s" or  line[-1] == "z":
            line = line + "es"
        elif line[-2] not in vowels and line[-1] == "y":
            line = line[:-1] + "ies"
        elif line[-1] == "f":
            line = line[:-1] + "ves"
        elif line[-2:] == "fe":
            line = line[:-2] + "ves"
        elif line[-1] == "o":
            line = line + "es"
        else:
            line = line + "s"
        print(line)

if __name__ == '__main__':
    main()
