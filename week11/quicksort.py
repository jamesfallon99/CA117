from quicksort_112 import quicksort
import random

def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    quicksort(A, 0, len(A)-1)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()