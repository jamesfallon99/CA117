from rpn_092 import calculator
import sys

def main():

    for line in sys.stdin:
        try:
            a = calculator(line.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()