'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
'''

import heapq

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        tmp = heapq.nlargest(3, nums)
        oneL, twoL, threeL = tmp[0], tmp[1], tmp[2]
        tmp2 = heapq.nsmallest(2, nums)
        oneS, twoS = tmp2[0], tmp2[1]
        
        return max(oneL*twoL*threeL, oneL*oneS*twoS)
