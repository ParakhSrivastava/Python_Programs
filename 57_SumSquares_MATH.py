'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=(int)(c**0.5)
        temp=c
        while (sq>=0):
            d=sq**2
            if d<=temp:
                temp=temp-d
                sq-=1
            else:
                sq-=1
        if temp==0:
            return "True"
        else:
            return "False"
            
