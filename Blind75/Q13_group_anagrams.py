from typing import List

"""
https://leetcode.com/problems/group-anagrams/description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in freq_map:
                word_lst = freq_map[sorted_word]
                word_lst.append(word)
                freq_map[sorted_word] = word_lst
            else:
                freq_map[sorted_word] = [word]
        result = [freq_map[key] for key in freq_map]
        return result
