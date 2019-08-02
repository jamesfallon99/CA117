#!/usr/bin/env python3

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
