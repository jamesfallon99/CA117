#!/usr/bin/env python3

def sort_on(t):
    return t.name

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)

class Triathlon(object):

    def __init__(self):
        self.triathlon = {}

    def add(self, triathlete):
        self.triathlon[triathlete.tid] = triathlete

    def remove(self, tid):
        del self.triathlon[tid]

    def lookup(self, tid):
        if tid in self.triathlon:
            return self.triathlon[tid]
        else:
            return None

    def __str__(self):
        r = ["{}".format(t) for t in sorted(self.triathlon.values(), key=sort_on)]
        return "\n".join(r)
