# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:15:07 2019

@author: admin
"""
import DataProcessing

def subarray_with_given_sum(data):
    """
    The first line of input contains an integer T denoting the number of test 
    cases. Then T test cases follow. Each test case consists of two lines. 
    The first line of each test case is N and S, where N is the size of array 
    and S is the sum. The second line of each test case contains N space 
    separated integers denoting the array elements.
    
    return list of results
    """
    n_test = int(data.split("\n")[0])
    first_line, second_line = DataProcessing.prepareData(data)
    results = []
    for i in range(n_test):
        n, s = list(map(int, first_line[i].split()))
        array = list(map(int, second_line[i].split()))
        for i in range(len(array)):
            for j in range(0, i):
                if sum(array[j:i+1]) == s:
                    results.append("{} to {} for {}".format(j+1,i+1, s))
                else:
                    continue
    return results
    
            
        
        
    