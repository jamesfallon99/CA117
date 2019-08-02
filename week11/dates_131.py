import sys

def main():
    months = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    for line in sys.stdin:
        tokens = line.strip().split()
        date = tokens[0] + "/" + months[tokens[1]] + "/" + tokens[2][2:]
        print(date)
if __name__ == '__main__':
    main()
