#!/usr/bin/env python3

def find():
    low = bottom
    high = top

    while low < high:
        mid = (low + high) // 2

        if guess(mid) == -1:
            low = mid + 1
        else:
            high = mid

    return low

if __name__ == '__main__':
    main()
