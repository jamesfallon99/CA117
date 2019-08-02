#!/usr/bin/env python3

import sys

def three(N):
    return [n for n in range(1, N + 1) if n % 3 == 0]

def squares(N):
    return[n ** 2 for n in range(1, N + 1) if n % 3 == 0]

def double(N):
    return[n * 2 for n in range(1, N + 1) if n % 4 == 0]

def three_or_four(N):
    return[n for n in range(1, N + 1) if n % 3 == 0 or n % 4 == 0]

def three_and_four(N):
    return[n for n in range(1, N + 1) if n % 3 == 0 and n % 4 == 0]

def replaced(N):
    return["X" if n % 3 == 0 else n for n in range(1, N + 1)]

def prime(N):
    return[n for n in range(1, N + 1) if n == 2 or n == 3 or n == 5 or n == 7 or (n > 1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0)]

def main():
    N = int(sys.argv[1])
    print("Multiples of 3: {}".format(three(N)))
    print("Multiples of 3 squared: {}".format(squares(N)))
    print("Multiples of 4 doubled: {}".format(double(N)))
    print("Multiples of 3 or 4: {}".format(three_or_four(N)))
    print("Multiples of 3 and 4: {}".format(three_and_four(N)))
    print("Multiples of 3 replaced: {}".format(replaced(N)))
    print("Primes: {}".format(prime(N)))

if __name__ == '__main__':
    main()
