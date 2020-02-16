'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: 
            return head
        prev = dummy = ListNode(0)
        dummy.next = head

        for i in range(m-1):
            prev=prev.next       
        cur = first = prev.next       
        temp = None    
        for i in range(n-m+1):
            next = cur.next
            cur.next = temp
            temp = cur
            cur = next

        prev.next = temp
        if cur:
            first.next = cur

        return dummy.next
        
