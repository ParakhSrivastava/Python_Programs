'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==0:
            return 0
        elif n<=2:
            return min(cost)
        dp=[cost[0],cost[1]]
        for i in range(2,n):
            dp.append(min(dp[i-1],dp[i-2])+cost[i])
        return min(dp[-1],dp[-2])
