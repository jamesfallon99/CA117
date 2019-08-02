#!/usr/bin/env python3

def reverse_list(l):
    if len(l) == 0:
        new_lis = []
        return new_lis

    new_lis = reverse_list(l[1:])
    new_lis.append(l[0])
    return new_lis
