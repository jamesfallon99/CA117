#!/usr/bin/env python3

import sys

def main():
    errors = []
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            line = line.strip().split()
            lis = []
            n = line[0]
            base = line[1]
            try:
                while int(n) != 0:
                    lis.append(int(n) % int(base))
                    n = int(n) // int(base)
                total = 0
                for item in lis:
                    total = total + (int(item) ** 2)
                print(total)
            except:
                errors.append(int(count))
    finally:
        if sum(errors) > 0:
            a = ("Failed to convert line(s):" + " " + str(errors)[1:-1] + " ")
            print(a)

if __name__ == '__main__':
    main()
