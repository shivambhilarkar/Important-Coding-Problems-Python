from typing import Optional

"""
https://leetcode.com/problems/validate-binary-search-tree/description/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.inorder_traversal(root, result)
        for index in range(1, len(result)):
            if result[index] <= result[index - 1]:
                return False
        return True

    def inorder_traversal(self, root: TreeNode, result: list) -> int:
        if root == None:
            return
        self.inorder_traversal(root.left, result)
        result.append(root.val)
        self.inorder_traversal(root.right, result)
