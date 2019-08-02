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
    
    matches = {
               3: 0,
               4: 0,
               5: 0,
               6: 0
    }

    for num in range(amount):
        random_sample = set(random.sample(number_range, draw))
        match = len(s.intersection(random_sample)) 
        if match < 3:
            continue
        else:
            matches[match] += 1
    
    for k, v in matches.items():
        lis = []
        for v in matches.items():
            lis.append(v)
        print(lis)

    
    print("Match 3's : {} ({} to 1)".format(value, value / amount))


if __name__ == '__main__':
    main()

