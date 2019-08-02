#!/usr/bin/env python3

import sys
def main():
    try:
        with open(sys.argv[1]) as f:
            bestmark = -1
            for line in f:
                mark, name = line.strip().split(" ", 1)
                if int(mark) > int(bestmark):
                    bestmark, beststudents = int(mark), name
                elif int(mark) == int(bestmark):
                    beststudents = beststudents + ", " + name
            print("Best student(s): {}".format(beststudents))
            print("Best mark: {}".format(bestmark))
    except FileNotFoundError:
        print("could not open that")

if __name__ == '__main__':
    main()
