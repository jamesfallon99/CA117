#!/usr/bin/env python3

import sys

def main():
    d = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "one hundred"
    }
    for line in sys.stdin:
        tokens = line.strip().split()
        lis = []
        for nums in tokens:
            if len(nums) == 2 and int(nums) > 19 and int(nums) % 10 != 0:
                lis.append(d[int(nums[0]) * 10] + "-" + d[int(nums[1])])
            else:
                lis.append(d[int(nums)])
        print(" ".join(lis))

if __name__ == '__main__':
    main()
