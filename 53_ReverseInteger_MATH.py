'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
'''

import math

class Solution:
    def reverse(self, x: int) -> int:
        
        if (x > 0):
            is_negative = False
        else: 
            is_negative = True
        
        reversed_integer = [char for char in str(abs(x))]
        
        reversed_integer.reverse()
        
        if is_negative == True:
            reversed_integer.insert(0, '-')

        result = int(''.join(reversed_integer))
        
        if math.pow(-2, 31) <= result <= (math.pow(2, 31) - 1):
            return result
        else:
            return 0
