'''
Input: 1->2->3
Output: 1->2->4
'''

class Solution:
  def plusOne(self, List):
    dummy=Node(0)
    dummy.next=head
    not_nine=dummy
    while head:
      if head.val!=9:
        not_nine=head
      head=head.next
    not_nine.val+=1
    not_nine=not_nine.next
    while not_nine:
      not_nine.val=0
      not_nine=not_nine.next
    if dummy.val:     
      return dummy
    else:
      return dummy.next
