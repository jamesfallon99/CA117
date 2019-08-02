from bank_082 import BankAccount

def main():

    # Check class attributes
    print('Checking class attributes...')
    print(BankAccount.next_account_number)
    print(BankAccount.total_lodgements)
    print(BankAccount.interest_rate)

    # Create two accounts
    b1 = BankAccount('Persephone', 'Murphy')
    b2 = BankAccount('Jemima', 'O\'Reilly', 30)

    # Check string representation
    print('Printing bank accounts...')
    print(b1)
    print(b2)

    # Check lodge
    print('Checking lodgements...')
    b1.lodge(100)
    b2.lodge(100)
    print(b1)
    print(b2)

    # Check increment
    print('Checking increment...')
    b3 = b1
    b1 += 22
    b2 += 23
    print(b1)
    print(b3 is b1)
    print(b2)

    # Check interest
    b1.apply_interest()
    b2.apply_interest()
    print(b1)
    print(b2)

    # Check class attributes
    print('Checking class attributes...')    
    print(BankAccount.next_account_number)
    print(BankAccount.total_lodgements)
    print(BankAccount.interest_rate)

if __name__ == '__main__':
    main()