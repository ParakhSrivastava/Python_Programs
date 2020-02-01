'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        stck=[]
        slow, fast=head,head
        while fast and fast.next:
            stck.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        while (slow and len(stck)):
            if stck.pop()!=slow.val:
                return False
            slow=slow.next
        return True
                
