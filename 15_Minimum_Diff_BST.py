'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        self.inorder(root,output)
        mini_diff = float('inf')
        # for unbounded upper value
        for i in range(1,len(output)):
            mini_diff = min(mini_diff,output[i]-output[i-1])
        return mini_diff
        
    def inorder(self,root,output):
        if root == None:
            return 
        else:
         # In increasing Order
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
