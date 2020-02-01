'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, current = None, head
        while current:
            if current.val == val:
                if prev:
                    # Remove the current node in the normal way.
                    prev.next = current.next
                    current = prev
                    # Advance the prev pointer.
                    prev = current
                else:
                    # We are at the head, advance the head and keep prev as None.
                    head = head.next
            else:
                # Advance the prev pointer.
                prev = current
            # Advance the current pointer.
            current = current.next
        return head
