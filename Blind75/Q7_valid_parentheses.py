"""
https://leetcode.com/problems/valid-parentheses/description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        return self.is_valid_parentheses(s)

    def is_valid_parentheses(self, text: str) -> bool:
        stack = []
        for ch in text:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == ']' and stack.pop() != '[':
                    return False
                if ch == ')' and stack.pop() != '(':
                    return False
                if ch == '}' and stack.pop() != '{':
                    return False
        return len(stack) == 0
