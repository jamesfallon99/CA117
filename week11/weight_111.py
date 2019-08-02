#!/usr/bin/env python3

class Weight(object):

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)

    OUNCES_PER_POUND = 16

    def from_ounces(ounces):
        pounds = ounces // Weight.OUNCES_PER_POUND
        leftover_ounces = ounces % Weight.OUNCES_PER_POUND
        return Weight(pounds, leftover_ounces)

    def total_ounces(self):
        return (self.pounds * 16 + self.ounces)

    def __ne__(self, other):
        return self.pounds, self.ounces != other.pounds, other.ounces

    def __eq__(self, other):
        return self.pounds, self.ounces == other.pounds, other.ounces

    def __lt__(self, other):
        return self.pounds, self.ounces < other.pounds, other.ounces

    def __ge__(self, other):
        return self.pounds, self.ounces >= other.pounds, other.ounces

    def __add__(self, other):
        return Weight.from_ounces(self.total_ounces() + other.total_ounces())

    def __iadd__(self, other):
        new_weight = Weight.from_ounces(self.total_ounces() + other.total_ounces())
        self.pounds, self.ounces = new_weight.pounds, new_weight.ounces
        return self

    def __mul__(self, num):
        return Weight.from_ounces(self.total_ounces() * num)
