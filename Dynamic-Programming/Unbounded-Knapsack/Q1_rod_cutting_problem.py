# max profit rod cutting
# https://www.geeksforgeeks.org/problems/rod-cutting0840/1
"""
Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by
cutting in two pieces of lengths 2 and
6, i.e., 5+17=22.
"""


class Solution:
    def recursive_rod_cuts(self, lengths: list, prices: list, index: int) -> int:
        pass

    def tabulation_rod_cuts(self, length: int, prices: list) -> int:
        lengths = [i for i in range(1, length + 1)]
        dp = [[0 for _ in range(length + 1)] for _ in range(len(prices) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if lengths[i - 1] <= j:
                    dp[i][j] = max(prices[i - 1] + dp[i][j - lengths[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(prices)][length]


if __name__ == '__main__':
    pass
