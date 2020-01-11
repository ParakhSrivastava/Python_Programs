'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:return []
        self.res = collections.defaultdict(list)
        self.freq = collections.defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            self.freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        for key,value in self.freq.items():
            self.res[value].append(key)
        
        return self.res[max(self.res.keys())]
        
