from weight_111 import Weight

def main():

    # Create some weights
    w1 = Weight()
    w2 = Weight(6, 4)
    w3 = Weight.from_ounces(100)

    # Confirm all are instances of Weight
    assert(isinstance(w1, Weight))
    assert(isinstance(w2, Weight))
    assert(isinstance(w3, Weight))
    
    # Ounces per pound
    print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))

    # Display weights
    print('Weights...')
    print(w1)
    print(w2)
    print(w3)

    # Check relations
    assert(w1 != w2)
    assert(w2 == w3)
    assert(w1 < w2)
    assert(w3 > w1)
    assert(w2 >= w3)

    # Addition
    print('Addition...')
    w4 = w2 + w3
    assert(isinstance(w4, Weight))
    print(w4)

    # In-place addition
    print('In-place addition...')
    w2_alias = w2
    w2 += w3
    assert(w2 is w2_alias)
    print(w2)

    # Multiplication
    print('Multiplication...')
    w5 = w3 * 3
    assert(isinstance(w5, Weight))
    print(w5)

if __name__ == '__main__':
    main()