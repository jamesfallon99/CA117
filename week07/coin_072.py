#!/usr/bin/env python3

from random import randint

class Coin(object):

    def __init__(self, sideup="Heads"):
        self.sideup = sideup

    def flip(self):
        x = randint(0, 1)
        if x:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def getstate(self):
        return self.sideup

    def __str__(self):
       return "Current state : {}".format(self.sideup)
