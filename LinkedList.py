# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:40:24 2019

@author: admin
"""

class node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        
class LinkedList:
    def __init__(self):
        self.headVal = None
    
    # Create a print LinkedList method
    def printList(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal
            
    # Create a get middle LinkedList element method
    def getMiddle(self):
        if self.headVal is None:
            return "LinkedList is None"
        else:
            mid = self.headVal
            avg = self.getLength() -1
            if (avg % 2) == 0:
                for _ in range(round(avg/2)):
                    mid = mid.nextVal
            else:
                for _ in range(round(avg/2)):
                    mid = mid.nextVal
                return "{} or {}".format(mid.dataVal, mid.nextVal.dataVal)
            return mid.dataVal
    
    # Create a get length of LinkedList method
    def getLength(self):
        if self.headVal is None:
            return "List is empty so length is None"
        else:
            count = 1
            l_len = self.headVal 
            while(l_len.nextVal):
                count += 1
                l_len = l_len.nextVal
            return count
        
    # Create get node method    
    def getVal(self, n):
        if self.headVal is None:
            return "No LinkedList"
        else:
            temp = self.headVal
            for _ in range(n-1):
                if temp.nextVal:
                    temp = temp.nextVal
                else:
                    return "End"
            return temp
        
    # Create get next node method
    def getNextVal(self):
        if self.headVal is None:
            return "None"
        else:
            next_node = self.headVal.nextVal
        return next_node.dataVal
    """
    def getRotate(self, r):
        if self.headVal is None:
            return "No LinkedList"
        else:
            temp = self.headVal
            for i in range(0, self.getLength(), r):
                temp = self.getVal(i)
                self.headVal = temp
    """
    """
    def getNumberVal(self, s, e):
        if self.headVal is None:
            return "LinkedList is None"
        else:
            temp = self.headVal
            for _ in range(s, e):
                temp = temp.nextVal
            
            self.headVal = temp
    """                
    # Create get data value method
    def getDataVal(self, n):
        return n.dataVal
    
    # Create insert node at beginning method
    def insertBeginning(self,n_node):
        new_node = node(n_node)
        if self.headVal is None:
            self.headVal = new_node
        else:
            start = new_node
            start.nextVal = self.headVal
            self.headVal = start
    
    # Create insert node in between method
    def insertBetween(self, n, n_node):
        new_node = node(n_node)
        if self.headVal is None:
            self.headVal = new_node
        else:
            if n is None:
                print("Please provide a starting node to add a next node")
                return
            else:
                temp = self.headVal
                for _ in range(n-1):
                    temp = temp.nextVal
                new_node.nextVal = temp.nextVal
                temp.nextVal = new_node
    
    # Create insert node at the end method
    def insertEnd(self, n_node):
        new_node = node(n_node)
        if self.headVal is None:
            self.headVal = new_node
        else:
            end = self.headVal
            while(end.nextVal):
                end = end.nextVal
            end.nextVal = new_node
       
# Create the LinkedList method
def createList(array, n):
    linkedList = LinkedList()
    for i in range(n):
        linkedList.insertEnd(array[i])
    return linkedList
    
if __name__=='__main__':
    t = 2
    n = [5,6]
    array = [[1,2,3,4,5], [2,3,6,7,5,1]]
    rotate = [2,2]
    for i in range(t):        
        head = createList(array[i], n[i])
        #head.getRotate(rotate[i])
        print(head.printList())