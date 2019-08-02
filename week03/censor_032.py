#!/usr/bin/env python3

import sys

def main():
    lis = []
    file = sys.argv[1]
    with open(file, "r") as f:
        censored_words = f.read().strip().split()

    for line in sys.stdin:
        lis.append(line.strip())
    for line in lis:
        line = line.split()
        new_lis = []
        for word in line:
            for censored in censored_words:

                if censored in censored_words:
                    word = word.replace(censored, "@" * len(censored))
            new_lis.append(word)
        print(" ".join(new_lis))

if __name__ == '__main__':
    main()
