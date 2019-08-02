#!/usr/bin/env python3

import sys

def bsearch(a, q):
    low = 0
    high = len(a)

    while low < high:
        mid = (low + high) // 2
        if a[mid] < q:
            low = mid + 1
        elif a[mid] > q:
            high = mid
        else:
            return a[mid] == q

def main():
    words = [word.strip() for word in sys.stdin]
    wordslower = [word.lower() for word in words]

    print([word for word in words if len(word) >= 5 and bsearch(wordslower, word.lower()[::-1])])

if __name__ == '__main__':
    main()
