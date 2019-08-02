#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    maximum_num = maximum(l[:-1])
    if l[-1] > maximum_num:
        return l[-1]
    else:
        return maximum_num
