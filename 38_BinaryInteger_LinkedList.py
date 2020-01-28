'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node=head
        c=0
        while node:
            c+=1
            node=node.next
        node=head
        s=0
        while node:
            s= s + node.val*(2**(c-1))
            c-=1
            node=node.next
        return s
