#!/usr/bin/env python3

class Customer(object):

    discount = 0

    def __init__(self, name, balance, addr1, addr2, addr3):
        self.name = name
        self.balance = balance
        self.address_line1 = addr1
        self.address_line2 = addr2
        self.address_line3 = addr3

    def owes(self):
       return self.balance * ((100 - self.discount) / 100)

    def __str__(self):
        l = []
        l.append("{}".format(self.name))
        l.append("{}".format(self.address_line1))
        l.append("{}".format(self.address_line2))
        l.append("{}".format(self.address_line3))
        l.append("Balance: {:.2f}".format(self.balance))
        l.append("Discount: {}%".format(self.discount))
        l.append("Amount due: {:.2f}".format(self.owes()))
        return "\n".join(l)

class ValuedCustomer(Customer):
    discount = 10
