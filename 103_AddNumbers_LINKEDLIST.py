'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        s1,s2,s3 = [],[],[]
        t=0
        r=None
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        if len(s1)<len(s2): 
            s1 = [0 for i in range( len(s2)-len(s1) ) ] + s1
        else:
            s2 = [0 for i in range( len(s1)-len(s2) ) ] + s2
            
        for i in range(len(s1)):
            s = s1[-1-i] + s2[-1-i] + t
            s3 += [s%10]
            t = s//10
            
        if t>0:
            s3 += [t]
        
        for i in s3:
            t=ListNode(i)
            t.next=r
            r = t
            
        return r
        
