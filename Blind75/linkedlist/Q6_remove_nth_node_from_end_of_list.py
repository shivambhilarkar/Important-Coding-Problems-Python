"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description
Given the head of a linked list,
remove the nth node from the end of the list and return its head.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(-1, head)
        dummy = result
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return result.next
