"""
https://leetcode.com/problems/3sum/description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        return self.get_three_sum(nums)

    def get_three_sum(self, nums: list) -> list:
        nums = sorted(nums)
        result_set = set()
        for index in range(0, len(nums) - 1):
            start = index + 1
            end = len(nums) - 1
            while start < end:
                current_sum = nums[index] + nums[start] + nums[end]
                if current_sum == 0 and index != start and start != end:
                    result_set.add((nums[index], nums[start], nums[end]))
                if current_sum < 0:
                    start += 1
                else:
                    end -= 1
        result = []
        for item in result_set:
            result.append([item[0], item[1], item[2]])
        return result
