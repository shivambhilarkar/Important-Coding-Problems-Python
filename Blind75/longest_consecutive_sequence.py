from typing import List
"""
https://leetcode.com/problems/longest-consecutive-sequence/description/
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        num_set = set()
        num_set.update(nums)

        for num in nums:
            if num - 1 not in num_set:
                current_num = num + 1
                current_length = 1
                while current_num in num_set:
                    current_length += 1
                    current_num = current_num + 1
                longest_length = max(longest_length, current_length)
        return longest_length

