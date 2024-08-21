# Definition for singly-linked list.
from heapq import heappush, heappop
from typing import List, Optional

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val  # TODO how this works ?

        min_heap = []
        for lst in lists:
            if lst:
                heappush(min_heap, lst)
        merged_head = ListNode(-1)
        temp = merged_head
        while min_heap:
            current_node = heappop(min_heap)
            temp.next = current_node
            temp = temp.next
            if current_node.next:
                heappush(min_heap, current_node.next)
        return merged_head.next
