# https://leetcode.com/problems/next-greater-element-ii/description/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.get_next_greater_element_circular(nums)

    def get_next_greater_element_circular(self, nums: list) -> list:
        stack = []
        length = len(nums)
        result = [-1] * length
        for index in range(0, 2 * length):
            current_element = nums[index % length]
            while len(stack) != 0 and nums[stack[-1]] < current_element:
                current_index = stack.pop()
                result[current_index] = current_element
            stack.append(index % length)
        return result

    def get_next_greater_element(self, nums: list) -> list:
        stack = []
        length = len(nums)
        result = [-1] * length
        for index in range(0, length):
            current_element = nums[index]
            while len(stack) != 0 and nums[stack[-1]] < current_element:
                current_index = stack.pop()
                result[current_index] = current_element
            stack.append(index)
        return result
