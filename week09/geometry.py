from geometry_091 import Triangle, Square, Point

def main():

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()