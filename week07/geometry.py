from geometry_072 import Point, Segment, Circle

def main():
    p1 = Point()
    p2 = Point(5, 5)
    s1 = Segment(p1, p2)
    s2 = Segment(p2, p1)
    c1 = Circle(p1, 5)
    c2 = Circle(p2, 2)
    c3 = Circle(p1, 2)

    print(p1)
    print(p2)
    print(s1.midpoint())
    print(s2.midpoint())
    print(c1.overlaps(c2))
    print(c2.overlaps(c1))
    print(c1.overlaps(c3))
    print(c3.overlaps(c2))

if __name__ == '__main__':
    main()