# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Node:
    def __init__(self,val="a",next=None):
        self.val=val
        self.next=None
length=0
class Solution:
    def mergeTwoLists(self, list1: object[ListNode], list2: object[ListNode]) ->object[ListNode]:
        i=list1
        j=list2
        new=Node()
        temp=new
        global length
        while i!=None and j!=None:
            if(i.val<=j.val):
                temp.val=i.val
                x=Node()
                temp.next=x
                temp=temp.next
                i=i.next
                length+=1
            else:
                temp.val=j.val
                x=Node()
                temp.next=x
                temp=temp.next
                j=j.next
                length+=1
        while j!=None:
            temp.val=j.val
            x=Node()
            temp.next=x
            temp=temp.next
            j=j.next
            length+=1

        while i!=None:
            temp.val=i.val
            x=Node()
            temp.next=x
            temp=temp.next
            i=i.next
            length+=1
        temp=new 
        if(temp.val=="a"):
            return None
        while(temp.next.val!="a"):
            temp=temp.next
        temp.next=None
        return new           
