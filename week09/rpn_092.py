#!/usr/bin/env python3

from stack_092 import Stack
from math import sqrt
import sys

def add(x, y):
    return (x + y)
def sub(x, y):
    return (x - y)
def mul(x, y):
    return (x * y)
def div(x, y):
    return(x / y)
def negative(x):
    return -x

uniops = {
    "r": sqrt,
    "n": negative
}

binops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator(line):
    stack = Stack()
    tokens = line.split()
    for c in tokens:
        if c in binops.keys():
            y = stack.pop()
            x = stack.pop()
            stack.push(binops[c](x, y))
        elif c in uniops.keys():
            stack.push(uniops[c](stack.pop()))
        else:
            stack.push(float(c))
    return stack.top()


if __name__ == '__main__':
    main()
