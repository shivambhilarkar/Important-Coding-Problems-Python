# Palindrome partition - min number of partitions required.

class Solution:
    def __is_palindrome(self, text: str, start: int, end: int) -> bool:
        word = text[start:end + 1]
        return word == word[::-1]

    def recursive_partition(self, text: str, start: int, end: int) -> int:
        if start >= end:
            return 0
        if self.__is_palindrome(text, start, end):
            return 0
        minimum = float('inf')
        for k in range(start, end):
            temp = self.recursive_partition(text, start, k) + self.recursive_partition(text, k + 1, end) + 1
            minimum = min(minimum, temp)
        return minimum

    def memoization_partition(self, text: str, start: int, end: int, dp) -> int:
        if start >= end:
            return 0
        if dp[start][end] is not None:
            return dp[start][end]
        if self.__is_palindrome(text, start, end):
            return 0
        minimum = float('inf')
        for k in range(start, end):
            temp = self.memoization_partition(text, start, k, dp) + self.memoization_partition(text, k + 1, end, dp) + 1
            minimum = min(minimum, temp)
        dp[start][end] = minimum
        return dp[start][end]

    def memoization_partition_optimise(self, text: str, start: int, end: int, dp) -> int:
        if start >= end:
            return 0
        if dp[start][end] is not None:
            return dp[start][end]
        if self.__is_palindrome(text, start, end):
            return 0
        minimum = float('inf')
        for k in range(start, end):
            if self.__is_palindrome(text, start, k):
                temp = self.memoization_partition_optimise(text, k + 1, end, dp) + 1
                minimum = min(minimum, temp)
        dp[start][end] = minimum
        return dp[start][end]


if __name__ == '__main__':
    # return self.recursive_partition(s, 0, len(s) - 1)
    # s = "word"
    # dp = [[None for _ in range(len(s))] for _ in range(len(s))]
    # return self.memoization_partition(s, 0, len(s) - 1, dp)
    pass
