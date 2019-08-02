#!/usr/bin/env python3

from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

class Shape(object):

    def __init__(self, list_points):
        self.list_points = list_points

    def sides(self):
        length = []
        for i in range(1, len(self.list_points)):
            length.append(self.list_points[i - 1].distance(self.list_points[i]))

        length.append(self.list_points[-1].distance(self.list_points[0]))
        return length

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):

    def area(self):
        sides = self.sides()
        s = sum(sides) / 2
        return sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))

class Square(Shape):

    def area(self):
        return self.sides()[0] ** 2
