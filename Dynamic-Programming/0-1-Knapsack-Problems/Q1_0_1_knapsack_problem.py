# 0-1 knapsack problem
# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
# how to define 2D matrix?
# java - int[row][col]
# python - [ [ 0 for _ in range(col)] for _ range(row) ]

class Solution:
    # recursive approach
    def recursive_0_1_knapsack(self, weights: list, values: list, max_weight: int, n: int) -> int:
        if n == 0 or max_weight == 0:
            return 0
        if weights[n - 1] <= max_weight:
            take_current = values[n - 1] + self.recursive_0_1_knapsack(weights, values, max_weight - weights[n - 1], n - 1)
            dont_take = self.recursive_0_1_knapsack(weights, values, max_weight, n - 1)
            return max(take_current, dont_take)
        else:
            return self.recursive_0_1_knapsack(weights, values, max_weight, n - 1)

    # memoization approach
    def memoization_0_1_knapsack(self, weights: list, values: list, max_weight: int, n: int, dp) -> int:
        if n == 0 or max_weight == 0:
            return 0

        if dp[n][max_weight] != 0:
            return dp[n][max_weight]

        if weights[n - 1] <= max_weight:
            take = values[n - 1] + self.memoization_0_1_knapsack(weights, values, max_weight - weights[n - 1], n - 1, dp)
            dont_take = self.memoization_0_1_knapsack(weights, values, max_weight, n - 1, dp)
            result = max(take, dont_take)
        else:
            result = self.memoization_0_1_knapsack(weights, values, max_weight, n - 1, dp)
        dp[n][max_weight] = result
        return dp[n][max_weight]

    # tabular approach / top-down approach
    def tabular_0_1_knapsack(self, weights: list, values: list, max_weight: int, n: int) -> int:
        dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if weights[i - 1] <= j:
                    take = values[i - 1] + dp[i - 1][j - weights[i - 1]]
                    dont_take = dp[i - 1][j]
                    dp[i][j] = max(take, dont_take)
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][max_weight]


if __name__ == '__main__':
    max_weight = 10
    n = 5
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    pass
