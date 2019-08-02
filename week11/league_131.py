import sys

def sorter(t):
    return t[1]

def main():
    lis = []
    d = {}
    for line in sys.stdin:
        tokens = line.strip().split()
        try:
            total = int(tokens[-1]) + int(tokens[-2]) + int(tokens[-3]) + int(tokens[-4]) + int(tokens[-5])
        except ValueError:
            continue
        teams = " ".join(tokens[0:-5])
        lis.append(len(teams))
        d[teams] = total

        largest = len(str(max(d.values())))

    for k, v in sorted(d.items(), key=sorter, reverse=True):
        print("{:>{}} {:>{}} points".format(k, max(lis), v, largest))

if __name__ == '__main__':
    main()
