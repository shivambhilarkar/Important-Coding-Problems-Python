# longest palindromic subsequence

class Solution:

    def tabulation_lcs(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]

    def tabulation_solution(self, text1: str) -> int:
        text1 = text1
        text2 = text1[::-1]
        return self.tabulation_lcs(text1, text2)


if __name__ == '__main__':
    pass
