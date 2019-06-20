# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:32:08 2019

@author: admin
"""
# My this solution consider the input not sorted so at line 27, you might
# encounter TLE errors. To change whole list elements will cost more so 
# in the case of already sorted list, please remove sorted and map functions.

def rearrange_list(array, array_size):
    a_l = len(array)
    a_i = 0
    new_array = []
    length = a_l/2
    while a_l-1 >= length:
        new_array.append(array[a_l-1])
        new_array.append(array[a_i])
        a_i += 1
        a_l -= 1
    if (array_size%2) == 1:
        new_array.append(array[int(array_size/2)])
    return new_array


test_cases = int("1")
for _ in range(test_cases):
    array_size = int("11")
    array = sorted(map(int, "10 20 30 40 50 60 70 80 90 100 110".split()))
    new_array = rearrange_list(array, array_size)
    print(new_array)