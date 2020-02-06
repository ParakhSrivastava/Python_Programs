'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2^0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and int((bin(n)+'0')[3:], 2) == 0
