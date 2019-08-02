#!/usr/bin/env python3

class Element(object):

    def chemical_element(self, num, name, sym, boil):
        self.number = num
        self.name = name
        self.symbol = sym
        self.boiling_point = boil

    def print_details(self):
        print("Number: {}".format(self.number))
        print("Name: {}".format(self.name))
        print("Symbol: {}".format(self.symbol))
        print("Boiling point: {} K".format(self.boiling_point))

    def __init__(self, num=None, name=None, sym=None, boil=None):
        self.number = num
        self.name = name
        self.symbol = sym
        self.boiling_point = boil
