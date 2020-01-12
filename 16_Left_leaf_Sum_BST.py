'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, flag:bool=False) -> int:
        if not root:
            return 0
        if not root.left and not root.right and flag:
            return root.val
        return self.sumOfLeftLeaves(root.left, True)+self.sumOfLeftLeaves(root.right, False)
