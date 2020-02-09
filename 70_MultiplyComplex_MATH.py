'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
'''


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_r = int(a[:a.index('+')])
        a_c = int(a[a.index('+')+1:-1])
        b_r = int(b[:b.index('+')])
        b_c = int(b[b.index('+')+1:-1])
        res = str(a_r*b_r-a_c*b_c)+"+"+str(a_r*b_c+a_c*b_r)+"i"
        return res
