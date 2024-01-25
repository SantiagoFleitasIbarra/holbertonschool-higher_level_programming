#!/usr/bin/python3

for abc in range(97, 123):
    if (chr(abc) != 'e' and chr(abc) != 'q'):
        print("{}".format(chr(abc)), end='')