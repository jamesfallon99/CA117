from employee_082 import Employee

def main():

    # Check class attributes
    print('Checking class attributes...')
    print(Employee.next_employee_number)
    
    # Create two employees
    e1 = Employee('Jimmy')
    e2 = Employee('Mary', hours_worked=12, hourly_rate=12.40)

    # Check string representation
    print('Printing employees...')
    print(e1)
    print(e2)

    # Check adding hours
    print('Checking adding hours...')
    e1.add_hours(10.5)
    e2.add_hours(30)
    print(e1)
    print(e2)

    # Check class attributes
    print('Checking class attributes...')    
    print(Employee.next_employee_number)

if __name__ == '__main__':
    main()