'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = int(a,2)
        dec_b = int(b,2)
        result = dec_a+dec_b
        return (str(bin(result)[2:]))
