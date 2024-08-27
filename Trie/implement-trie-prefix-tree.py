"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_ending = False

class Trie:
    root = None

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.is_ending = True

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                return False
            temp = temp.children[index]
        if temp is not None and temp.is_ending == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                return False
            temp = temp.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
