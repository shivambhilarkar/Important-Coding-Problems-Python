from typing import List

"""
https://leetcode.com/problems/set-matrix-zeroes/description
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
                 
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        col_length = len(matrix[0])
        rows = [False for _ in range(row_length)]
        cols = [False for _ in range(col_length)]
        for r in range(row_length):
            for c in range(col_length):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for r in range(row_length):
            for c in range(col_length):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
