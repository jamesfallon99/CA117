import sys
import math

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    i = start_r
    while i <= end_r:
        radius = i
        area = 4 * math.pi * radius ** 2
        volume = (4 * math.pi * radius ** 3) / 3.0
        print("{:>10.1f} {:>15.2f} {:>15.2f}".format(radius, area, volume))
        i = i + inc_r


if __name__ == '__main__':
    main()
