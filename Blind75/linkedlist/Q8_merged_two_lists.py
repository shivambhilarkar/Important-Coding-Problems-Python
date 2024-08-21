from typing import Optional

"""
https://leetcode.com/problems/merge-two-sorted-lists/description
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode(-1)
        temp = merged_head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1 is not None:
            temp.next = list1
        if list2 is not None:
            temp.next = list2
        return merged_head.next
