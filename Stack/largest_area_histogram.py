# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.largest_reactangle_in_histogram(heights)

    def largest_reactangle_in_histogram(self, heights: list) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for index in range(0, n + 1):
            while len(stack) != 0 and (index == n or heights[stack[-1]] >= heights[index]):
                height = heights[stack.pop()]
                width = 0
                if len(stack) == 0:
                    width = index
                else:
                    width = index - stack[-1] - 1
                area = height * width
                max_area = max(area, max_area)
            stack.append(index)
        return max_area
