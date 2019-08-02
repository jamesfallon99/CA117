#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip().lower()
        for c in line:
            if not c.isalnum():
                line = line.replace(c, "")
        backwards = line[::-1].strip()
        if line == backwards:
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    main()
