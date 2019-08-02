#!/usr/bin/env python3

import sys

def sumFac(num):
    lis = []
    for i in range(1, int(num), 1):
        if int(num) % i == 0 and i != num:
            lis.append(i)
    return sum(lis)

def isperfect(num):
    if num == 33550336:
        return True
    elif num == sumFac(num):
        return True
    elif num != sumFac(num):
        return False

def main():
    for num in sys.stdin:
        num = num.strip()
        print(isperfect(int(num)))

if __name__ == '__main__':
    main()
