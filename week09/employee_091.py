#!/usr/bin/env python3

class Employee(object):

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return 0

    def __str__(self):
        l = []
        l.append("Name: {}".format(self.name))
        l.append("Number: {}".format(self.number))
        l.append("Wages: {:.2f}".format(self.wages()))
        return "\n".join(l)


class Manager(Employee):
    def __init__(self, name, number, salary):
        super().__init__(name, number)
        self.salary = salary

    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    def __init__(self, name, number, hourly_rate, hours):
        super().__init__(name, number)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def wages(self):
        return self.hourly_rate * self.hours
