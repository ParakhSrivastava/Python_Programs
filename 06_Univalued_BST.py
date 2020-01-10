'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root,root.val)
    
    def helper(self,root,val):
        if root is None:
            return True
        if root.val!=val:
            return False
        return self.helper(root.left,val) and self.helper(root.right,val)
        
