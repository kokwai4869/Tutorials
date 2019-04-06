# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:36:21 2019

@author: admin
"""
from itertools import permutations

def get_longest_palindrome(data):
    n_test = data[0]
    data = data[1]
    string_list = []
    for i in range(n_test):
        string_list.append(data[i])
    for i in range(len(string_list)):
        to = []
        for string in string_list:
            for i in range(len(string)):
                for j in range(0,i):
                    ss = string[j:i+1]
                    reverse = ss[::-1]
                    if ss == reverse:
                        to.append(ss)
    return max(to,key=len)

def reverse_string_words(data):
    n_test = data[0]
    data = data[1]
    results = []
    for i in range(n_test):
        results.append(".".join(reversed(data[i].split("."))))
    return results

def permutation_of_given_strings(data):
    n_test = data[0]
    data = data[1]
    results = []
    for i in range(n_test):
        results.append(" ".join(list(map(lambda x: "".join(x),
                                         permutations(data[i])))))
    return results

def recursively_remove_all_adjacent_duplicates(data):
    n_test = data[0]
    data = data[1]
    results = []
    for i in range(n_test):
        sentence = []
        for index_c in range(len(data[i])):
            if data[i][index_c] != data[i][(index_c+1)%len(data[i])] \
            and data[i][index_c] != data[i][(index_c-1)%len(data[i])]:
                sentence.append(data[i][index_c])                
        results.append("".join(sentence))
    return results

def roman_number_to_integer(data):
    n_test = data[0]
    data = data[1]
    results = []
    dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    reverse = {value:key for key, value in dictionary.items()}
    for i in range(n_test):
        string_list = list(*[iter(data[i])])
        string_length = len(string_list)
        # Set the highest roman value as the middle character and get its index
        mid_highest_index = string_list.index(reverse[max([dictionary[x] for
                                                           x in string_list])])
        count = 0
        # We compare if the index is more than mid than we add otherwise minus
        for i in range(string_length):
            if i > mid_highest_index:
                count += dictionary[string_list[i]]
            elif i == mid_highest_index:
                count += dictionary[string_list[i]]
            else:
                count -= dictionary[string_list[i]]
        results.append(count)
    return results
                    
                    
            
    
