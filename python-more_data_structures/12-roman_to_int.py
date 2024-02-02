#!/usr/bin/python3

def roman_to_int(roman_string):

    result = 0
    prev_value = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    for numeral in reversed(roman_string):
        value = roman_num[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
