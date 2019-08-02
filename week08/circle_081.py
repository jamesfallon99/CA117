#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Centre: ({}, {})".format(self.x, self.y)

    def midpoint(self, other):
        return (self.x + other.x) / 2, (self.y + other.y) / 2

class Circle(object):

    def __init__(self, point=Point(0, 0), radius=0):
        self.radius = radius
        self.point = point

    def __str__(self):
        return "Centre: ({}, {})\nRadius: {}".format(self.point.x, self.point.y, self.radius)

    def __add__(self, other):
        new_radius = self.radius + other.radius
        new_x, new_y = Point.midpoint(self.point, other.point)

        return Circle(Point(new_x, new_y), new_radius)
