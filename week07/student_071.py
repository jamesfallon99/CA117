#!/usr/bin/env python3

class Student(object):

    def student(self, surname, forename, sid, modlist=""):
        self.student_ID = sid
        self.surname = surname
        self.forename = forename
        if modlist == "":
            modlist = []
        self.module_list = modlist

    def __init__(self, surname, forename, sid, modlist=""):
        self.student_ID = sid
        self.surname = surname
        self.forename = forename
        if modlist == "":
            modlist = []
        self.module_list = modlist

    def add_module(self, new):
        if new not in self.module_list:
            self.module_list.append(new)

    def del_module(self, old):
        if old in self.module_list:
            self.module_list.pop(self.module_list.index(old))

    def print_details(self):
        print("ID: {}".format(self.student_ID))
        print("Surname: {}".format(self.surname))
        print("Forename: {}".format(self.forename))
        print("Modules: {}".format(" ".join(self.module_list)))
