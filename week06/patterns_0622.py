#!/usr/bin/env python3

from re import findall
import sys

fin = open("patterns_062.txt")
s = fin.read()

phone = (r'\b\d{2}[-\s]\d{7}\b')
g = findall(phone, s)
print(g)

date = (r'\d{1,2}[/-]\d{1,2}[/-]\d{1,2}')
p = findall(date, s)
print(p)

email = (r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b')
e = findall(email, s)
print(e)

ldates = (r'\d{2}\s\w{3}\s\d{2}')
l = findall(ldates, s)
print(l)

