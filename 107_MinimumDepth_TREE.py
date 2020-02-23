
'''
BFS or Recursion
'''

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        
        # Agr root=None hi hai, to hme kuch ni krna h
        if root == None:
            return 0
        
        # Agr dono me se koi ek h ya dono hi ni h(children), to un dono me se max return krwana hai, kyuki min pe aage badhegi hi ni tree ki asli depth
        # 1 plus root ko count krne k lye kiya hai
        if root.left == None or root.right == None:
            return 1 + max(self.minDepth(root.left),self.minDepth(root.right))
        
        # Agr dono h, to dono children me se min wala hme return krana h
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
        
        '''
        class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        queue = []
        queue.append(root)
        height = 0
        while len(queue) > 0:
            height +=1
            for _ in range(len(queue)):
                node= queue.pop(0)
                if not node.left and not node.right:
                    return height
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return 0
        '''
