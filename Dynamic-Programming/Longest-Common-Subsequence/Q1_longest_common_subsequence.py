# longest common subsequence - LCS
# given two string find out longest common subsequence
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:

    def recursive_lcs(self, text1: str, n: int, text2: str, m: int) -> int:
        if n == 0 or m == 0:
            return 0
        if text1[n - 1] == text2[m - 1]:
            return self.recursive_lcs(text1, n - 1, text2, m - 1) + 1
        else:
            left = self.recursive_lcs(text1, n - 1, text2, m)
            right = self.recursive_lcs(text1, n, text2, m - 1)
            return max(left, right)

    def memoization_lcs(self, text1: str, n: int, text2: str, m: int, dp) -> int:
        if n == 0 or m == 0:
            return 0
        if dp[n][m] != 0:
            return dp[n][m]

        if text1[n - 1] == text2[m - 1]:
            result = self.memoization_lcs(text1, n - 1, text2, m - 1, dp) + 1
        else:
            left = self.memoization_lcs(text1, n - 1, text2, m, dp)
            right = self.memoization_lcs(text1, n, text2, m - 1, dp)
            result = max(left, right)
        dp[n][m] = result
        return dp[n][m]

    def tabulation_lcs(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]


if __name__ == '__main__':
    dp = [[0 for _ in range(len("text1") + 1)] for _ in range(len("text2") + 1)]
    solution = Solution()
    result = solution.memoization_lcs("text1", len("text1"), "text2", len("text2"))
