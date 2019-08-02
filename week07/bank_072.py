#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, bal=0):
        self.balance = bal

    def deposit(self, bal):
        self.balance = self.balance + bal

    def withdraw(self, bal):
        if self.balance >= bal:
            self.balance = self.balance - bal
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)
