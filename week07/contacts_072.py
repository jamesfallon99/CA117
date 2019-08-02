#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self):
        self.dictionary = {}

    def add_contact(self, contact):
        self.dictionary[contact.name] = contact

    def del_contact(self, contact):
        if contact in self.dictionary:
            del(self.dictionary[contact])

    def get_contact(self, contact):
        if contact in self.dictionary:
            return self.dictionary[contact]
        else:
            return None

    def __str__(self):
        string = "Contact list\n------------"
        for k in sorted(self.dictionary.keys()):
            string += "\n{}".format(self.dictionary[k])

        return string
