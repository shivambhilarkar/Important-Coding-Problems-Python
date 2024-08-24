# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversal = self.traverse(root)
        return level_order_traversal[::-1]  # we need to return reverse order in above question

    def traverse(self, root: TreeNode) -> list:
        if root == None:
            return []

        queue = deque()
        queue.append(root)
        result = []
        while len(queue) != 0:
            size = len(queue)
            row = []
            for _ in range(size):
                current_node = queue.popleft()
                row.append(current_node.val)
                if current_node.left != None:
                    queue.append(current_node.left)
                if current_node.right != None:
                    queue.append(current_node.right)
            result.append(row)
        return result
