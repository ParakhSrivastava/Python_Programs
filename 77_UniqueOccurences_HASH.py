'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
'''

from collections import Counter as C
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = C(arr)
        lis=set()
        c=0
        for k, v in hashmap.items():
            c+=1
            lis.add(v)
        if len(lis)==c:
            return True
