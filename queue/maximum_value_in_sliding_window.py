# Monotonic Queue
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.get_sliding_window_maximum(nums, k)

    def get_sliding_window_maximum(self, nums: list, k: int) -> list:
        queue = deque()
        result = []
        for index in range(0, len(nums)):
            current_element = nums[index]
            # remove out of range index from left side
            if queue and queue[0] <= index - k:
                queue.popleft()
            # remove smaller element index
            while queue and nums[queue[-1]] <= current_element:
                queue.pop()
            queue.append(index)

            if index >= k - 1:
                result.append(nums[queue[0]])
        return result
