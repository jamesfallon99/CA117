#!/usr/bin/env python3

import sys
import math
def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        a = int(tokens[0])
        b = int(tokens[1])
        c = int(tokens[2])
        try:
            x1 = (- b + math.sqrt((b ** 2) + (- 4 * a * c))) / (2 * a)
            x2 = (- b - math.sqrt((b ** 2) + (- 4 * a * c))) / (2 * a)
            print("r1 = {}, r2 = {}".format(x1, x2))
        except ValueError:
            print(None)


if __name__ == '__main__':
    main()
