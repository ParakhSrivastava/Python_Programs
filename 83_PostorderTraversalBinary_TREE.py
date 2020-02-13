'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        temp = [root]
        res = []
        
        # PREORDER
        while temp:
            node=temp.pop()
            res.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        # POSTORDER by reversing
        return res[::-1]
