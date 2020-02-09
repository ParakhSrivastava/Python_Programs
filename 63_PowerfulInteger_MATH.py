'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xset, yset = collections.OrderedDict(), collections.OrderedDict()
        
        if x == 1:
            xset[1] = 1
        else:
            i = 0
            while x**i < bound:
                xset[x**i] = 1
                i += 1
                
        if y == 1:
            yset[1] = 1
        else:
            j = 0
            while y**j < bound:
                yset[y**j] = 1
                j += 1
                
        ans = []
        for n in range(bound+1):
            for x in xset:
                if x >= n:
                    break
                if (n - x) in yset:   
                    ans.append(n)
                    break
        return ans
