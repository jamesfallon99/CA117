#!/usr/bin/env python3

def swap_keys_values(d):
    new_d = {}
    for k, v in d.items():
        new_d[v] = k
    return new_d
