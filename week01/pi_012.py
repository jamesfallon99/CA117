#!/usr/bin/env python3

import sys
import math
def main():
    n = int(sys.argv[1])
    print('{:.{}f}'.format(math.pi, n))

if __name__ == '__main__':
    main()
