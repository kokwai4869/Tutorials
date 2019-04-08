# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:36:21 2019

@author: admin
"""
from itertools import permutations
from collections import Counter

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

def anagram(data):
    n_test = data[0]
    data = data[1]
    results = []
    for i in range(n_test):
        first, second = data[i].split()
        if "".join(sorted(first)) == "".join(sorted(second)):
            results.append("YES")
        else:
            results.append("NO")
    return results

def longest_common_substring(data):
    n_test = data[0]
    data = data[1]
    results = []
    partitions = round(len(data)/n_test)
    for i in range(0, len(data), partitions):
        len_first, len_second = data[i].split()
        first = data[i+1]
        second = data[i+2]
        # This is too expensive and need to edit but Im just too lazy to think
        substring_first = [first[j:i+1] for i in range(len(first)) for
                           j in range(0,i)] + list(*[iter(first)])
        substring_second = [second[j:i+1] for i in range(len(second)) for
                           j in range(0,i)] + list(*[iter(second)])
        similar = list(map(lambda x: len(x),
                           set(substring_second).intersection(
                                   set(substring_first))))
        results.append(max(similar))
    return results
            
def longest_common_prefix_in_an_array(data):
    # Alright, this is SUPER EXPENSIVE, I still need to improve! NEED EDIT!
    #Im freaking lazy!!!
    n_test = data[0]
    data = data[1]
    results = []
    partitions = round(len(data)/n_test)
    for i in range(0, len(data), partitions):
        string_list = data[i+1].split()
        result = []
        for ii in range(int(data[i])):
            index = 1
            for iii in range(len(string_list[ii])):
                if string_list[ii][:index] in \
                string_list[(ii+1)%len(data[i])][:index]:
                    result.append(string_list[ii][:index])
                index += 1
        result_count = Counter(result)
        dictionary_word_count = {word:count for
                                     word,count in result_count.items()}
        common_prefix_count_value = max(dictionary_word_count.values())
        common_prefix_result = []
        for word,count in dictionary_word_count.items():
            if count == common_prefix_count_value:
                common_prefix_result.append(word)
        results.append(max(common_prefix_result,key=len))
    return results

def merge_the_tools(data):
    """
    Input: original data and not prepared data.
    """
    data = data.split("\n")
    string, k = data[0], int(data[1])
    results = []
    for part in zip(*[iter(string)]*k):
        d = dict()
        value = "".join([d.setdefault(x,x) for x in part if x not in d])
        results.append(value)
    return results
    