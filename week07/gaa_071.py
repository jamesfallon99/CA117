#!/usr/bin/env python3

class Score(object):

    def __init__(self, g=0, p=0):
        self.goals = g
        self.points = p

    def greater_than(self, other):
        return self.goals * 3 + self.points > other.goals * 3 + other.points

    def less_than(self, other):
        return self.goals * 3 + self.points < other.goals * 3 + other.points

    def equal_to(self, other):
        return self.goals * 3 + self.points == other.goals * 3 + other.points
