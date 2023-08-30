#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1 = head
        cur2 = head
        while True:
            if not cur1 or not cur1.next or \
                not cur2 or not cur2.next or not cur2.next.next:
                return False
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
# @lc code=end
