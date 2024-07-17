from typing import List


# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = set()
        for i in range(len(triplets)):
            # eliminate toxic tuple
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            for j in range(3):
                if triplets[i][j] == target[j]:
                    result.add(j)
        return len(result) == 3
