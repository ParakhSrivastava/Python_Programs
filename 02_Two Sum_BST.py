'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nums = set()
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        if (k - root.val) in self.nums:
            return True
        else:
            self.nums.add(root.val)

        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
