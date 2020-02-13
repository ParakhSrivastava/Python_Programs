'''
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
       def postorder(self, root):
        if not root:
            return []
        
        stack=[root]
        ans=[]
        while stack:
            cur_node=stack.pop()
            ans=[cur_node.val]+ans
            for child in cur_node.children:
                stack.append(child)
        return ans
        
