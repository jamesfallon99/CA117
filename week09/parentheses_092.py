#!/usr/bin/env python3

from stack_092 import Stack
import sys

lefties = "({["
righties = ")}]"

def other_bracket(b):
    if b in lefties:
        return righties[lefties.index(b)]
    return lefties[righties.index(b)]

def matcher(line):
    stack = Stack()
    for c in line:
        if c in lefties:
            stack.push(c)
        elif c in righties:
            if stack.is_empty():
                return False
            if stack.top() != other_bracket(c):
                return False

            stack.pop()
    return stack.is_empty()
