#!/usr/bin/env python3

import sys

def main():
    total0 = 0.0
    total1 = 0.0
    total2 = 0.0
    total3 = 0.0
    total4 = 0.0
    total5 = 0.0
    total6 = 0.0
    total7 = 0.0
    total8 = 0.0
    total9 = 0.0
    total = 0.0
    for line in sys.stdin:
        line = line.strip()
        if int(line[-1]) == 0:
            total0 = total0 + 1.0
        elif int(line[-1]) == 1:
            total1 = total1 + 1.0
        elif int(line[-1]) == 2:
            total2 = total2 + 1.0
        elif int(line[-1]) == 3:
            total3 = total3 + 1.0
        elif int(line[-1]) == 4:
            total4 = total4 + 1.0
        elif int(line[-1]) == 0:
            total0 = total0 + 1.0
        elif int(line[-1]) == 5:
            total5 = total5 + 1.0
        elif int(line[-1]) == 6:
            total6 = total6 + 1.0
        elif int(line[-1]) == 7:
            total7 = total7 + 1.0
        elif int(line[-1]) == 8:
            total8 = total8 + 1.0
        elif int(line[-1]) == 9:
            total9 = total9 + 1.0
    total = total + total0 + total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9
    print("The probability of nothing is {:.4f}%".format(total0 / total * 100))
    print("The probability of one pair is {:.4f}%".format(total1 / total * 100))
    print("The probability of two pairs is {:.4f}%".format(total2 / total * 100))
    print("The probability of three of a kind is {:.4f}%".format(total3 / total * 100))
    print("The probability of a straight is {:.4f}%".format(total4 / total * 100))
    print("The probability of a flush is {:.4f}%".format(total5 / total * 100))
    print("The probability of a full house is {:.4f}%".format(total6 / total * 100))
    print("The probability of four of a kind is {:.4f}%".format(total7 / total * 100))
    print("The probability of a straight flush is {:.4f}%".format(total8 / total * 100))
    print("The probability of a royal flush is {:.4f}%".format(total9 / total * 100))
if __name__ == '__main__':
    main()
