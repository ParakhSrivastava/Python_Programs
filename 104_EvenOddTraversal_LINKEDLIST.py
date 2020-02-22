'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        odd=[]
        even=[]
        r=None
        c=0
        if not head:
            return
        while head:
            c+=1
            if c%2==0:
                even=[head.val]+even
            else:
                odd=[head.val]+odd
            head=head.next
        for i in odd:
            t=ListNode(i)
            t.next=r
            r=t
        head=r
        j=None
        while head.next:
            head=head.next
        for i in even:
            t=ListNode(i)
            t.next=j
            j=t
        head.next=j
        return r
    '''
        even_head = None
        prev = None
        curr = head
        while curr != None:
            
            even = curr.next
            
            if even != None:
                if even_head == None:
                    even_head = even
                    
                curr.next = even.next
                even.next = None if even.next == None else even.next.next
            
            prev = curr
            curr = curr.next
        
        if prev != None: 
            prev.next = even_head
            
        return head
