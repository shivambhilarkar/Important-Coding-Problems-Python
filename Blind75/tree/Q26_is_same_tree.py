from typing import Optional

"""
https://leetcode.com/problems/same-tree/description
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)
        return left_subtree and right_subtree
