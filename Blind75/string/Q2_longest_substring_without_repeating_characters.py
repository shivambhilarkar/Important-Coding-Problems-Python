"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest
substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.get_longest_substring(s)

    def get_longest_substring(self, text: str) -> int:
        freq_map = dict()
        front = 0
        rear = 0
        result = 0
        while front < len(text):
            current_char = text[front]
            if current_char in freq_map:
                while current_char in freq_map:
                    del freq_map[text[rear]]
                    rear += 1
            freq_map[current_char] = 1
            result = max(front - rear + 1, result)
            front += 1
        return result


if __name__ == '__main__':
    pass
