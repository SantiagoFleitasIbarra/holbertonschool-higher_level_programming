#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_num = set()
    total = 0
    for num in my_list:
        if num not in uniq_num:
            uniq_num.add(num)
            total += num
    return total
