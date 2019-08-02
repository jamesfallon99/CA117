#!/usr/bin/env python3

import sys
def main():
    for line in sys.stdin:
        line = line.strip()
        try:
            print("Thank you for {}".format(int(line)))
            break
        except ValueError:
            print("{} is not a number".format(line))
if __name__ == '__main__':
    main()
