'''
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        if not head:
            return [0]
        
        node = head
        
        # this stack will contain the elements that we don't know its next greater node
        # alongside its index, to insert in correct place
        stack = [(0, node.val)]
        node = node.next
        
        # starts the array with one element and increase it as we start iterating over the nodes
        result = [0] 
        i = 1
        while node:  # iterate over the linked list
            
            # do this until we find an element that is not greater that current node
            # or stack is empry
            while stack and node.val > stack[-1][-1]:
                    pos, val =  stack.pop()  # get index and value of top of stack
                    result[pos] = node.val  # update the greater element it the given index
            stack.append((i, node.val))
            node = node.next
            i += 1
            result.append(0)  # increase by 1 each new visited node
        
        # any element in the stack does not have a greater element
        while stack:
            pos, val = stack.pop()
            result[pos] = 0
        
        return result
        
