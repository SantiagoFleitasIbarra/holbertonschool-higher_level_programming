#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num_args = len(sys.argv) - 1
    plural = 's' if num_args != 1 else ''

    if (num_args == 0):
        print("0 arguments.")
    else:
        print(f"{num_args} argument{plural}:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
