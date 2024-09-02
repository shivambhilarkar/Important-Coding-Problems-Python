# Trie for bit manipulation
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
from typing import List


class Node:
    def __init__(self):
        self.links = [None] * 2


class BitTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, number: int) -> None:
        node = self.root
        for bit_no in range(31, -1, -1):
            bit = (number >> bit_no) & 1
            if node.links[bit] is None:
                node.links[bit] = Node()
            node = node.links[bit]

    def get_max_xor(self, number: int) -> None:
        node = self.root
        max_xor = 0
        for bit_no in range(31, -1, -1):
            bit = (number >> bit_no) & 1
            if node.links[bit - 1] is not None:
                max_xor = max_xor | (1 << bit_no)
                node = node.links[bit - 1]
            else:
                node = node.links[bit]
        return max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = BitTrie()
        for num in nums:
            trie.insert(num)

        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, trie.get_max_xor(num))
        return max_xor
