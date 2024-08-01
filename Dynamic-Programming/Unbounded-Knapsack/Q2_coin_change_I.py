# https://leetcode.com/problems/coin-change-ii/solutions/3685532/simple-dp-solution-using-python/
# https://leetcode.com/problems/coin-change-ii/description/
"""
Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: list) -> int:
        return self.tabulation_coin_change(amount, coins)

    def tabulation_coin_change(self, amount: int, coins: list) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(1, len(dp)):
            if i != 0:
                dp[i][0] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(coins)][amount]


if __name__ == '__main__':
    pass
