"""
https://leetcode.com/problems/container-with-most-water/description/
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container,
such that the container contains the most water.
Return the maximum amount of water a container can store.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        self.get_maximum_water(height)

    def get_maximum_water(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(current_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(f"max area : {max_area}")
        return max_area


if __name__ == '__main__':
    pass
