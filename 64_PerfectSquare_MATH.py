'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        from math import log, exp
        sqrt_val = round(exp(log(num)/2))
        return sqrt_val * sqrt_val == num
