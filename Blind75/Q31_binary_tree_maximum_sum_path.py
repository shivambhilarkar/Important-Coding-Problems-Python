from typing import Optional

"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description
A path in a binary tree is a sequence of nodes where each pair of
adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [float('-inf')]
        self.get_max_path(root, result)
        return result[0]

    def get_max_path(self, node: TreeNode, result) -> int:
        if node == None:
            return 0

        left_subtree = self.get_max_path(node.left, result)
        right_subtree = self.get_max_path(node.right, result)

        current_is_path = left_subtree + right_subtree + node.val
        current_is_not_path = max(left_subtree, right_subtree) + node.val
        current_is_start = node.val

        current_max_path = max(current_is_path, current_is_not_path, current_is_start)
        result[0] = max(current_max_path, result[0])
        return max(current_is_not_path, current_is_start)
