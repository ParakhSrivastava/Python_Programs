'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
'''

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        lvl = math.ceil(math.log10(label+1)/math.log10(2))
        out=[]
        out.append(label)
        for i in range(lvl,2,-1):
            temp=(2**(i-2))-1
            temp2=(2**(i-1))-1
            label=(label//2)
            label=temp+(temp2-label)+1
            out.insert(0,label)
        out.insert(0,1)
        return out
