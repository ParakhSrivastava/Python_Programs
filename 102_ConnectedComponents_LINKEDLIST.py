'''
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ans = 0
        Gset = set(G)
        c = 0 # counting the length of current connected components
        while head:
            if head.val not in Gset: 
                if c > 0: # end of an existing connected component
                    ans += 1
                c = 0 # reset c
            else: 
                c += 1
            head = head.next
        if c > 0: # the last connected component may end at the end of the linked list
            ans += 1
        return ans
