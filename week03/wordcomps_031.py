#!/usr/bin/env python3

import sys

def seventeen(line):
    return[l for l in line if len(l) == 17]

def more_seventeen(line):
    return[l for l in line if len(l) > 17]

def allvowels(line):
    return(min([l for l in line if all(c in l for c in ["a", "e", "i", "o", "u"])], key=len))

def fouras(line):
    return[l for l in line if l.lower().count("a") == 4]

def twoqs(line):
    return[l for l in line if l.lower().count("q") >= 2]

def cie(line):
    return[l for l in line if "cie" in l]

def anagram(line):
    return[l for l in line if all(c.lower() in l.lower() for c in ["a", "n", "g", "l", "e"]) and len(l) == 5 and l != "angle"]

def iary(line):
    return(len([l for l in line if l.lower().count("iary")]))

def mostes(line):
    most = 0
    for l in line:
        if l.lower().count("e") > most:
            most = l.lower().count("e")
    return[l for l in line if l.count("e") == most]

def main():
    lines = [l.strip() for l in sys.stdin]
    vowels = "aeiou"

    print("Words containing 17 letters: {}".format(seventeen(lines)))
    print("Words containing 18+ letters: {}".format(more_seventeen(lines)))
    print("Shortest word containing all vowels: {}".format(allvowels(lines)))
    print("Words with 4 a's: {}".format(fouras(lines)))
    print("Words with 2+ q's: {}".format(twoqs(lines)))
    print("Words containing cie: {}".format(cie(lines)))
    print("Anagrams of angle: {}".format(anagram(lines)))
    print("Words ending in iary: {}".format(iary(lines)))
    print("Words with most e's: {}".format(mostes(lines)))

if __name__ == '__main__':
    main()
