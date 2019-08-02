#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.points)

    def total_points(self):
        return (self.goals * 3) + (self.points)

    def __eq__(self, other):
        return self.total_points() == other.total_points()

    def __gt__(self, other):
        return self.total_points() > other.total_points()

    def __ge__(self, other):
        return self.total_points() >= other.total_points()

    def __add__(self, other):
        total_goal = self.goals + other.goals
        total_point = self.points + other.points
        return Score(total_goal, total_point)

    def __sub__(self, other):
        total_goal = self.goals - other.goals
        total_point = self.points - other.points
        return Score(total_goal, total_point)

    def __iadd__(self, other):
        total_goal = self.goals + other.goals
        total_point = self.points + other.points
        self.goals, self.points = total_goal, total_point
        return self

    def __isub__(self, other):
        total_goal = self.goals - other.goals
        total_point = self.points - other.points
        self.goals, self.points = total_goal, total_point
        return self
