#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return "Name: {}\nID: {}".format(self.name, self.tid)
