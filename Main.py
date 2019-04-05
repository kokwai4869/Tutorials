# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:11:50 2019

@author: admin
"""
import DataProcessing
import MethodsLinkedList

d = DataProcessing
data = d.readText("data/3.txt")
t = int(data.split("\n")[0])
n = list(map(int, data.split("\n")[1].split(" ")))
array = list(map(lambda x: list(map(int, x.split(" "))), data.split("\n")[2:]))
#rotate = [2,2]
for i in range(t):        
    head = MethodsLinkedList.createList(array[i], n[i])
    #head.getRotate(rotate[i])
    print(head.printList())