"""
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


# TODO: solve with diagonal approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longest_palindromic_substring(s)

    def longest_palindromic_substring(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_length = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(dp)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_length:
                        max_length = i - j + 1
                        max_str = s[j:i + 1]
        return max_str


if __name__ == '__main__':
    pass
