'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        a=5
        s=0
        flag=0
        while (n//a)!=0:
            s+=n//a
            a*=5
        return s
