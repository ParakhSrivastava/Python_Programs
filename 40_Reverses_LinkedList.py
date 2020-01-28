'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None  # previous node
        cur = head  # current node
        while cur:  # iteratively
            nxt = cur.next  # save the next node
            cur.next = pre  # reverse
            # go ahead
            pre = cur
            cur = nxt
        return pre
