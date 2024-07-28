# longest common substring
# given two string find out longest common substring
# TODO : Memoization approach

class Solution:
    def recursive_longest_common_substring(self, text1: str, n: int, text2: str, m: int, max_count: int) -> int:
        if n == 0 or m == 0:
            return max_count
        if text1[n - 1] == text2[m - 1]:
            max_count = self.recursive_longest_common_substring(text1, n - 1, text2, m - 1, max_count + 1)

        left = self.recursive_longest_common_substring(text1, n - 1, text2, m, 0)
        right = self.recursive_longest_common_substring(text1, n, text2, m - 1, 0)
        max_count = max(max_count, left, right)
        return max_count

    def tabulation_longest_common_substring(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        result = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = 0
        return result


if __name__ == '__main__':
    pass
