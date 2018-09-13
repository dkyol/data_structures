# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:06:00 2018

implementation of single link list 
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        
        count = 1
        current = self.head
        if position == 1:
            return current 
        while current:
            
            count += 1
            current = current.next
            if (count == position):
                return current
                break
        return None
    

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

#prints value of appended elements 
print (ll.get_position(1).value)
print (ll.get_position(2).value)
print (ll.get_position(3).value)