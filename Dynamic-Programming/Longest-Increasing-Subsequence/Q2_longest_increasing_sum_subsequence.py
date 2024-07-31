# longest increasing subsequence sum
# lis = longest increasing subsequence
# https://www.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1
# TODO : lis problem https://leetcode.com/problems/best-team-with-no-conflicts/description/

class Solution:
    def recursive_lis_sum(self, nums: list, index:int, previous_element:int) -> int:
        if index >= len(nums):
            return 0
        take = 0
        if nums[index] > previous_element:
            take = self.recursive_lis_sum(nums, index+1, nums[index]) + nums[index]
        dont_take = self.recursive_lis_sum(nums, index+1, previous_element)
        return max(take, dont_take)

    def memoization_lis_sum(self, nums:list, index:int, previous_element:int, dp:list) -> int:
        if index >= len(nums):
            return 0

        take = 0
        if nums[index] > previous_element:
            if dp[index] == float('-inf'):
                dp[index] = self.memoization_lis_sum(nums, index+1, nums[index], dp) + nums[index]
            take = dp[index]
        dont_take = self.memoization_lis_sum(nums, index+1, previous_element, dp)
        return max(take, dont_take)


if __name__ == '__main__':
    pass
