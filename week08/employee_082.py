#!/usr/bin/env python3

class Employee(object):
    next_employee_number = 0

    def __init__(self, name, hours_worked=0, hourly_rate=9.25):
        self.name = name
        self.id = Employee.next_employee_number
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        Employee.next_employee_number += 1

    def add_hours(self, other):
        self.hours_worked += other

    def __str__(self):
        return "Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}".format(self.name, self.id, self.hours_worked, self.hourly_rate, self.hourly_rate * self.hours_worked)
