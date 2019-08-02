#!/usr/bin/env python3

def minimum(l):
    if len(l) == 1:
        return l[0]

    minimum_num = minimum(l[:-1])
    if l[-1] < minimum_num:
        return l[-1]
    else:
        return minimum_num
