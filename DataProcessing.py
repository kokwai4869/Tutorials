# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:45:08 2019

@author: admin
"""

def readText(data):
    """
    Read from text file in data folder
    
    return string 
    """
    with open(data, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents

def prepareDataString(data):
    """
    Prepare data based on the lines
    
    return list of first and second lines
    """
    data_split = data.split("\n")
    n_test = int(data_split[0])
    test_cases = data_split[1:]
    first_line = []
    second_line = []
    for i in range(0, len(test_cases), 2):
        first_line.append(test_cases[i])
    for i in range(1, len(test_cases), 2):
        second_line.append(test_cases[i])
    return n_test, first_line, second_line