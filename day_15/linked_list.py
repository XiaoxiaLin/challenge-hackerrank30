#!/bin/python3

# Day 15


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data):
        if head is None:
            head = Node(data)
            self.tail = head
        else: 
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head
  


    def insert_rec(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head


    def insert1(self, head, data):
        # Complete this method
        node = Node(data)

        current = head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            head = node
        return head

# For a better understanding of the first insert function and the whole concept of linked list, it is recommended to read this post:
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#fig-addtohead

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
