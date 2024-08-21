from typing import Optional

"""
https://leetcode.com/problems/reverse-linked-list
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        next_node = None

        while head is not None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node
