#!/usr/bin/env python3

class Lamp(object):

    def lamp_on(self, on):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not(self.on)

    def __init__(self, on=False):
        self.on = on
