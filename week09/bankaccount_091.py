#!/usr/bin/env python3

class BankAccount(object):

    next_account_number = 16555232
    account_type = "General"

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, bal):
        self.balance += bal

    def withdraw(self, bal):
        if self.balance > bal:
            self.balance -= bal
        else:
            print("Insufficient funds available")

    def __str__(self):
        l = []
        l.append("Name: {} {}".format(self.forename, self.surname))
        l.append("Account number: {}".format(self.account_number))
        l.append("Account type: {}".format(self.account_type))
        l.append("Balance: {:.2f}".format(self.balance))
        return "\n".join(l)

class CurrentAccount(BankAccount):

    overdraft = -1000
    account_type = "Current"

    def withdraw(self, num):
        if self.balance - num >= -1000:
            self.balance -= num
        else:
            print("Insufficient funds available")

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append("Overdraft: {:.2f}".format(self.overdraft))
        return "\n".join(l)

class SavingsAccount(BankAccount):

    interest_rate = 0.01
    account_type = "Savings"

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

    def __str__(self):
        l = []
        l.append(super().__str__())
        l.append("Interest rate: {}".format(self.interest_rate))
        return "\n".join(l)
