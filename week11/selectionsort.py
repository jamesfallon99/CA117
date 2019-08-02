from selectionsort_112 import selectionsort
import random

def main():
    A = random.sample(range(-99, 100), 10)

    print('Unsorted: {}'.format(A))
    selectionsort(A)
    print('Sorted: {}'.format(A))

if __name__ == '__main__':
    main()