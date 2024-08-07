"""
https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.get_pairs(nums, target)

    def get_pairs(self, nums: list, target: int) -> list:
        freq_map = dict()
        for index, num in enumerate(nums):
            if target - num in freq_map:
                return [freq_map[target - num], index]
            freq_map[num] = index
        return [-1, -1]


if __name__ == '__main__':
    pass
