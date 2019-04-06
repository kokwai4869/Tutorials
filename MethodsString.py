# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:36:21 2019

@author: admin
"""
from itertools import permutations

import DataProcessing

def get_longest_palindrome(data):
    n_test = data[0]
    data = data[1:]
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
    data = data[1:]
    results = []
    for i in range(n_test):
        results.append(".".join(reversed(data[i][0].split("."))))
    return results

def permutation_of_given_strings(data):
    n_test = data[0]
    data = data[1:]
    results = []
    for i in range(n_test):
        results.append(" ".join(list(map(lambda x: "".join(x),
                                         permutations(data[i][0])))))
    return results

def recursively_remove_all_adjacent_duplicates(data):
    n_test = data[0]
    data = data[1:]
    results = []
    for i in range(n_test):
        sentence = []
        for index_c in range(len(data[i][0])):
            if data[i][0][index_c] != data[i][0][(index_c+1)%len(data[i][0])] \
            and data[i][0][index_c] != data[i][0][(index_c-1)%len(data[i][0])]:
                sentence.append(data[i][0][index_c])                
        results.append("".join(sentence))
    return results
