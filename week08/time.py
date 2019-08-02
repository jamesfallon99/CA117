from time_082 import Time

def main():

    t1 = Time()
    t2 = Time(9,35,16)
    t3 = Time(0,0,4)
    t4 = Time(9,35,16)

    # Check string representation
    print('Printing times...')
    print(t1)
    print(t2)
    print(t3)

    # Check equality
    print('Checking equality...')
    print(t2 == t4)
    print(t1 == t3)

    # Check greater than/less than
    print('Checking greater than/less than...')
    print(t2 > t3)
    print(t2 < t3)
    print(t4 > t1)
    print(t4 < t1)

    # Check addition
    print('Checking addition...')
    t5 = t2 + t2 + t2
    print(t5)
    print(t5 > t2)

    # Check increment
    print('Checking increment...')
    t33 = t2
    t2 += t2
    t2 += t4
    print(t2)
    print(t33 is t2)
    print(t2 > t3)
    
    # Check class method
    print('Checking class method...')
    t6 = Time.seconds_to_time(123456)
    print(t6)
    print(t6 > t1)

if __name__ == '__main__':
    main()