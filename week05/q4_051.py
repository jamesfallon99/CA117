#!/usr/bin/env python3

import sys

def main():
    nums = [int(line.strip()) for line in sys.stdin]
    total = sum(nums)
    mean = total / len(nums)
    if len(nums) % 2 != 0:
        median = sorted(nums)[len(nums) // 2]
    else:
        median = (sorted(nums)[len(nums) // 2] + sorted(nums)[len(nums) // 2 - 1]) / 2

    print("Mean: {:.1f}".format(mean))
    print("Median: {:.1f}".format(median))


if __name__ == '__main__':
    main()
