class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x *= -1
        self.y *= -1

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def reflect(self):
        self.p1.reflect()
        self.p2.reflect()

    def length(self):
        return self.p1.distance(self.p2)

    def __str__(self):
        return '{} to {} (length {:.1f})'.format(self.p1.__str__(), self.p2.__str__(), self.length())

def main():
    p1 = Point(3, 3)
    p2 = Point(3, 6)
    p3 = Point(10, 3)
    p4 = Point(3, 3)
    s1 = Segment(p1, p2)
    print('Segment 1: {}'.format(s1))
    s2 = Segment(p4, p3)
    print('Segment 2: {}'.format(s2))
    s1.reflect()
    print('Segment 1: {}'.format(s1))
    print('Segment 2: {}'.format(s2))

if __name__ == '__main__':
    main()
