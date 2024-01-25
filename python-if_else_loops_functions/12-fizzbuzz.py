#!/usr/bin/python3

def fizzbuzz():
    for ffizzbuzz in range(1, 101):
        if ((ffizzbuzz % 3) == 0 and (ffizzbuzz % 5) == 0):
            print("FizzBuzz ", end='')
        elif ((ffizzbuzz % 3) == 0):
            print("Fizz ", end='')
        elif ((ffizzbuzz % 5) == 0):
            print("Buzz ", end='')
        else:
            print("{} ".format(ffizzbuzz), end='')