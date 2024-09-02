# Trie for bit manipulation
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

class Node:
    def __init__(self):
        self.links = [None] * 2  # to store 2 bits 0 & 1


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
        max_xor_number = 0
        for bit_no in range(31, -1, -1):
            bit = (number >> bit_no) & 1
            if node.links[1 - bit]:
                max_xor_number = max_xor_number | (1 << bit)
                node = node.links[1 - bit]
            else:
                node = node.links[bit]
        return max_xor_number
