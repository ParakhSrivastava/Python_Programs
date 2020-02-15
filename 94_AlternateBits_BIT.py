'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=str(bin(n)[2:])
        flag=0
        for i in range(len(n)-1):
            if n[i]==n[i+1]:
                flag=1
        if flag==0:
            return True
