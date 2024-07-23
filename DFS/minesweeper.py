from typing import List


# https://leetcode.com/problems/minesweeper/
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(board) == 0 or len(board[0]) == 0 or len(click) != 2:
            return board
        x, y = click[0], click[1]
        if (board[x][y] == 'M'):
            board[x][y] = 'X'
            return board
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        self.dfs(board, x, y, len(board), len(board[0]), directions)
        return board

    def dfs(self, board, x, y, rows, cols, directions):
        if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != 'E':
            return
        adjacent_mine = self.get_adjacent_mine(board, x, y, rows, cols)
        if adjacent_mine > 0:
            board[x][y] = str(adjacent_mine)
        else:
            board[x][y] = 'B'
            for direction in directions:
                x1 = x + direction[0]
                y1 = y + direction[1]
                self.dfs(board, x1, y1, rows, cols, directions)

    def get_adjacent_mine(self, board, x, y, rows, cols):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                # if i >= 0 and i < rows and j >= 0 and j < cols and board[i][j] == 'M':
                #     count += 1
                # TODO : we can also write above condition like below
                if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'M':
                    count += 1
        return count
