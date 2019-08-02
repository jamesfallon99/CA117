#!/usr/bin/env python3

def sumup(n):
    if n == 0:
        return 0
    return n + sumup(n - 1)
