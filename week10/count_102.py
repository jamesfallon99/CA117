#!/usr/bin/env python3

def count_letters(s):

    if len(s) == 0:
        return 0
    else:
        return 1 + count_letters(s[:-1])
