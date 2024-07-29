# minimum number of insertion to make string a to b
# minimum number of deletion to make string a to b

class solution:
    def tabulation_lcs(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]

    def tabulation_minimum_no_of_insertion(self, text1: str, text2: str) -> int:
        lcs = self.tabulation_lcs(text1, text2)
        remaining_character = lcs - len(text1)
        return remaining_character

    def tabulation_minimum_no_of_deletion(self, text1: str, text2: str) -> int:
        lcs = self.tabulation_lcs(text1, text2)
        remaining_character = lcs - len(text1)
        return remaining_character


if __name__ == '__main__':
    pass
