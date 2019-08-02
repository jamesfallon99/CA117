#!/usr/bin/env python3

import random
import sys

six_nums = sys.argv[1:]
random.seed(42)
number_range = range(1, 47)
draw = 6
amount = 1000000

def main():
    s = set()
    for n in six_nums:
        s.add(int(n))
    match_three = 0
    match_four = 0
    match_five = 0
    match_six = 0


    for num in range(amount):
        random_sample = set(random.sample(number_range, draw))
        match = len(s.intersection(random_sample)) 
        if match < 3:
            continue
        elif match == 3:
            match_three += 1
        elif match == 4:
            match_four += 1
        elif match == 5:
            match_five += 1
        elif match == 6:
            match_six += 1
  
    print("Match 3's : {} ({} to 1)".format(match_three, amount / match_three ))
    print("Match 4's : {} ({} to 1)".format(match_four, amount / match_four))
    print("Match 5's : {} ({} to 1)".format(match_five, amount / match_five))
    print("Match 6's : {} ({} to 1)".format(match_six, match_six / amount))


if __name__ == '__main__':
    main()
