from priority_queue_112 import PQ

def main():

    pq = PQ()
    assert(pq.is_empty() == True)
    assert(pq.size() == 0)
    pq.insert(5)
    pq.insert(6)
    pq.insert(12)
    pq.insert(3)
    pq.insert(15)
    pq.insert(9)
    assert(pq.is_empty() == False)
    assert(pq.size() == 6)
    assert(pq.d[1] == 15)
    assert(pq.d[2] == 12)
    assert(pq.d[3] == 9)
    assert(pq.d[4] == 3)
    assert(pq.d[5] == 5)
    assert(pq.d[6] == 6)
    assert(pq.getMax() == 15)
    assert(pq.delMax() == 15)
    assert(pq.delMax() == 12)
    assert(pq.delMax() == 9)
    assert(pq.delMax() == 6)
    assert(pq.delMax() == 5)
    assert(pq.delMax() == 3)
    assert(pq.is_empty() == True)
    assert(pq.size() == 0)

if __name__ == '__main__':
    main()