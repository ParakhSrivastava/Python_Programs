'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
'''


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i=1
        s=0
        while num>0 and i <= math.sqrt(num):
            if (num % i == 0):
                if (num // i == i) : 
                    s+=i
                else : 
                    s+=i+num//i 
            i += 1
        s-=num
        if s==num and num!=0:
            return True
