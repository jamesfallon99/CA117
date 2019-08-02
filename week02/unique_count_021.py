#!/usr/bin/env python3

import sys
import string
def main():
    seen = []
    for line in sys.stdin:
        tokens = line.lower().strip().split()
        for word in tokens:
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter, "")
            if word not in seen:
                seen.append(word)
    print(len(seen) - 1)

if __name__ == '__main__':
    main()
