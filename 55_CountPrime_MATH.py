'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n):
        if n < 3: return 0
        dp = [0, 0] + [1] * (n - 2)
        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]: dp[i ** 2:n:i] = [0] * len(dp[i ** 2:n:i])
        return sum(dp)
