# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:36:21 2019

@author: admin
"""
import DataProcessing

def get_longest_palindrome(data):
    n_test = int(data.split("\n")[0])
    data = data.split("\n")[1:]
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
