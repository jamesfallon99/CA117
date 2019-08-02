import sys

def seconds(t):
    [mins, secs] = t.split(":")
    total_secs = int(mins) * 60 + int(secs)
    return total_secs

def sorter(t):
    return seconds(t[1])

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.split()
            d[tokens[0]] = min(tokens[1:], key=seconds)
        except ValueError:
            continue

    minimum = min(d.items(), key=sorter)
    print("{} : {}".format(minimum[0], minimum[1]))

if __name__ == '__main__':
    main()
