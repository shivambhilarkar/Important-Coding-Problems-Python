# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        for num in sorted(nums, reverse=True):
            total_sum -= num
            if total_sum > num:
                return total_sum + num
        return -1
