'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=n
        s,p=0,1
        while(m!=0):
            d = m % 10
            s=s+d
            p=p*d
            m=m//10
        return p-s
