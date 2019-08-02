import sys
import math

def main():
    lis = []
    total = 0
    for num in sys.stdin:
        num = num.strip()
        lis.append(num)
    for n in lis:
        total += float(n)

    mean = total / (len(lis))

    lis2 = []
    for n in lis:
        difference = float(n) - mean
        lis2.append(difference)

    lis3 = []
    for n in lis2:
        square = float(n) ** 2
        lis3.append(square)

    total2 = 0
    for n in lis3:
        total2 += float(n)

    stddev = math.sqrt(total2 / (len(lis3) - 1))
    print("Standard deviation: {:.3f}".format(stddev))


if __name__ == '__main__':
    main()
