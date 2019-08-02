#!/usr/bin/env python3

import sys
def main():
    try:
        highest = -1, ""
        file_name = sys.argv[1]
        lis = []
        with open(file_name, "r") as f:
            for line in f:
                tokens = line.strip().split()
                lis.append(tokens)

            for entry in lis:
                try:
                    if int(entry[0]) > int(highest[0]):
                        highest = entry
                except ValueError:
                    print("Invalid mark " + entry[0] + " encountered. Skipping.")
            name = " ".join(highest[1:])

            print("Best student: " + name)
            print("Best mark: " + highest[0])

    except FileNotFoundError:
        print('The file students ' + file_name + ' could not be opened.')

if __name__ == '__main__':
    main()
