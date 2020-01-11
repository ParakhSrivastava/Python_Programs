'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None: return 
        q=[root];res=[]
        while len(q)>0:
            n,s=len(q),0
            for i in range(n):
                x=q.pop(0)
                s+=x.val
                if x.left!=None:
                    q.append(x.left)
                if x.right!=None:
                    q.append(x.right)    
            res.append(s/n)
        return res        
