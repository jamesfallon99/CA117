from re import findall
import sys

from carreg_111 import car

def main():

    # Verify regular expression is not overly long
    assert(len(car) < 120)

    s = sys.stdin.read()
    
    carlist = findall(car, s)
    print('Cars: {}'.format(carlist))

if __name__ == '__main__':
    main()