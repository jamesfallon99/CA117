#!/usr/bin/env python3

class PQ(object):

    def __init__(self):
        self.d = {}
        self.N = 0

    def exch(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    def insert(self, v):
        self.N += 1
        self.d[self.N] = v
        self.swim(self.N)

    def swim(self, k):
        while k > 1 and self.d[k // 2] < self.d[k]:
            self.exch(k, k // 2)
            k = k // 2

    def bigger(self, i, j):
        try:
            return max([i, j], key=self.d.__getitem__)
        except KeyError:
            return i

    def delMax(self):
        v = self.d[1]
        self.exch(1, self.N)
        del(self.d[self.N])
        self.N -= 1
        self.sink(1)
        return v

    def sink(self, k):
        while (2 * k <= self.N):
            j = 2 * k
            j = self.bigger(j, j + 1)
            if self.d[k] >= self.d[j]:
                break
            self.exch(k, j)
            k = j

    def getMax(self):
        return self.d[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.N
