'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        S = set([
            0b1,
            0b100,
            0b10000,
            0b1000000,
            0b100000000,
            0b10000000000,
            0b1000000000000,
            0b100000000000000,
            0b10000000000000000,
            0b1000000000000000000,
            0b100000000000000000000,
            0b10000000000000000000000,
            0b1000000000000000000000000,
            0b100000000000000000000000000,
            0b10000000000000000000000000000,
            0b1000000000000000000000000000000
        ])
        return num in S
