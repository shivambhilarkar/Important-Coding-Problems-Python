# subset problem
# find out if subset is present with given sum
# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:

    def recursive_subset(self, N: int, arr: list, required_sum: int) -> bool:
        if N == 0 and required_sum != 0:
            return False
        if required_sum == 0:
            return True
        if arr[N - 1] <= required_sum:
            take = self.recursive_subset(N - 1, arr, required_sum - arr[N - 1])
            dont_take = self.recursive_subset(N - 1, arr, required_sum)
            result = take or dont_take
            return result
        else:
            dont_take = self.recursive_subset(N - 1, arr, required_sum)
            return dont_take

    def memoization_subset(self, N: int, arr: list, required_sum: int, dp) -> bool:
        if N == 0 and required_sum != 0:
            return False
        if required_sum == 0:
            return True
        if dp[N][required_sum] is not None:
            return dp[N][required_sum]

        if arr[N - 1] <= required_sum:
            take = self.memoization_subset(N - 1, arr, required_sum - arr[N - 1], dp)
            dont_take = self.memoization_subset(N - 1, arr, required_sum, dp)
            result = (take or dont_take)
        else:
            result = self.memoization_subset(N - 1, arr, required_sum, dp)
        dp[N][required_sum] = result
        return result

    def tabulation_subset(self, N: int, arr: list, required_sum: int) -> bool:
        dp = [[False for _ in range(required_sum + 1)] for _ in range(N + 1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if (i == 0 and j == 0) or j == 0:
                    dp[i][j] = True
                    continue
                elif i == 0:
                    dp[i][j] = False
                    continue

                if arr[i - 1] <= j:
                    take = dp[i - 1][j - arr[i - 1]]
                    dont_take = dp[i - 1][j]
                    dp[i][j] = take or dont_take
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[N][required_sum]


if __name__ == '__main__':
    # return self.recursive_subset(N, arr, sum)
    dp = [[None for _ in range(sum + 1)] for _ in range(N + 1)]
    # return self.memoization_subset(N, arr, sum, dp)
    pass
