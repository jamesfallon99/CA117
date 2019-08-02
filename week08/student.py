from student_081 import Student

def main():

    s1 = Student(15334499, 'Jones', 'Zoe')
    s1.add_mark('CA103', 71)
    s1.add_mark('CA106', 65)
    s1.add_mark('CA115', 84)
    s1.add_mark('CA116', 85)
    s1.add_mark('CA117', 70)
    s1.add_mark('CA169', 68)
    s1.add_mark('CA170', 74)
    s1.add_mark('CA172', 90)
    s1.add_mark('MS121', 50)

    s2 = Student(15667755, "Brent", "Tom")
    s2.add_mark('CA103', 55)
    s2.add_mark('CA106', 35)
    s2.add_mark('CA115', 70)
    s2.add_mark('CA116', 64)
    s2.add_mark('CA117', 66)
    s2.add_mark('CA169', 50)
    s2.add_mark('CA170', 55)
    s2.add_mark('CA172', 60)
    s2.add_mark('MS121', 35)

    s3 = Student(15112277, 'Brody', 'Joe')
    s3.add_mark('CA103', 35)
    s3.add_mark('CA106', 35)
    s3.add_mark('CA115', 60)
    s3.add_mark('CA116', 60)
    s3.add_mark('CA117', 60)
    s3.add_mark('CA169', 60)
    s3.add_mark('CA170', 60)
    s3.add_mark('CA172', 60)
    s3.add_mark('MS121', 60)

    print(s1)
    print(s2)
    print(s3)

if __name__ == '__main__':
    main()