#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    if (len(sys.argv) > 1):
        sum = 0
        for arg in sys.argv[1:]:
            sum += int(arg)
        print("{}".format(sum))
