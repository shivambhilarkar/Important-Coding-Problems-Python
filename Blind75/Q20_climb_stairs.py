"""
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0 for _ in range(n+1)]
        # return self.memoization_climb_stairs(n,dp)
        return self.tabulation_climb_stairs(n)

    def memoization_climb_stairs(self, n: int, dp: list) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if dp[n] != 0:
            return dp[n]
        one_steps = self.memoization_climb_stairs(n - 1, dp)
        two_steps = self.memoization_climb_stairs(n - 2, dp)
        dp[n] = one_steps + two_steps
        return dp[n]

    def tabulation_climb_stairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
