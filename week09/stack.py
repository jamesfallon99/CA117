from stack_092 import Stack

def main():

    s = Stack()

    print(len(s))
    s.push(1)
    print(s.top())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    try:
        print(s.pop())
    except IndexError:
        print('Error')
    try:
        print(s.top())
    except IndexError:
        print('Error')
    s.push(1)
    s.push(2)
    s.push(3)
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())   

if __name__ == '__main__':
    main()