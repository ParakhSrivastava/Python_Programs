'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recurse_tree(root)
        return root
    
    def switch_left_and_right(self, node: TreeNode) -> None:
        temp = node.left
        node.left = node.right
        node.right = temp
    
    def recurse_tree(self, node: TreeNode) -> None:
        if node:
            self.switch_left_and_right(node)
            self.recurse_tree(node.left)
            self.recurse_tree(node.right)        
