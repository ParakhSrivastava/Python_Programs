'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
    
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None
        elif node.val == val:
            return node
        elif node.val > val:
            return self.searchBST(node.left, val)
        else:
            return self.searchBST(node.right, val)        
