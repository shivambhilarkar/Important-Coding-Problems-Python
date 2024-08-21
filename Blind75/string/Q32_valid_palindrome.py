"""
https://leetcode.com/problems/valid-palindrome/description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for ch in s.lower():
            if 'a' <= ch <= 'z' or '0' <= ch <= '9':
                text += ch
        return text == text[::-1]
