#!/usr/bin/env python3

from priority_queue_112 import PQ
import sys

def main():
    m = int(sys.argv[1])
    pq = PQ()
    for x in sys.stdin:
        x = int(x.strip())
        if pq.size() < m:
            pq.insert(x)
            continue
        if x < pq.getMax():
            pq.delMax()
            pq.insert(x)
    while not pq.is_empty():
        print(pq.delMax())
if __name__ == '__main__':
    main()
