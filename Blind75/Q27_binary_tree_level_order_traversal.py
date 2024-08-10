from typing import Optional, List
from collections import deque

"""
https://leetcode.com/problems/binary-tree-level-order-traversal
Given the root of a binary tree, 
return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            row = []
            for item in range(size):
                current_node = queue.popleft()
                row.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            result.append(row)
        return result
