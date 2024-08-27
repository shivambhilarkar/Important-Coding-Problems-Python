"""
Trie data structure
https://wangyy395.medium.com/implement-a-trie-in-python-e8dd5c5fde3a
"""

class Node:
    def __int__(self):
        self.children = [None] * 26
        self.is_ending = False


class Trie:
    root = None

    def __init__(self):
        self.root = Node()

    # insert word into trie
    def insert_word(self, word: str) -> None:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.is_ending = True

    # search word from trie
    def search_word(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                return False
            temp = temp.children[index]
        if temp is not None and temp.is_ending is False:
            return False
        return True

    # check if any word is starting with given prefix
    def starts_with(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if temp.children[index] is None:
                return False
            temp = temp.children[index]
        return True
