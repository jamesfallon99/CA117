#!/usr/bin/env python3

def partition(A, p, r):
    q = j = p
    while j < r:
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[r] = A[r], A[q]
    return q

def quicksort(A, p, r):
    if r <= p:
        return

    q = partition(A, p, r)
    quicksort(A, p, q - 1)
    quicksort(A, q + 1, r)
