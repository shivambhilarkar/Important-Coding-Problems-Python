# longest increasing subsequence return length of longest subsequence
# reference : https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/

class Solution:
    def recursive_longest_subsequence(self, nums: list, index: int, previous_element: int) -> int:
        if index >= len(nums):
            return 0
        take = 0
        if nums[index] > previous_element:
            take = self.recursive_longest_subsequence(nums, index + 1, nums[index]) + 1
        dont_take = self.recursive_longest_subsequence(nums, index + 1, previous_element)
        return max(take, dont_take)

    def memoization_longest_subsequence(self, nums: list, index: int, previous_element: int, dp: list) -> int:
        if index >= len(nums):
            return 0
        take = 0
        if nums[index] > previous_element:
            if dp[index] == float('-inf'):
                dp[index] = self.memoization_longest_subsequence(nums, index + 1, nums[index], dp) + 1
            take = dp[index]
        dont_take = self.memoization_longest_subsequence(nums, index + 1, previous_element, dp)
        return max(take, dont_take)

    def tabulation_longest_subsequence(self, nums) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    dp = [float('-inf') for _ in range(len(nums))]
    solution = Solution()
    result = solution.memoization_longest_subsequence(nums, 0, float('-inf'), dp)
    pass
