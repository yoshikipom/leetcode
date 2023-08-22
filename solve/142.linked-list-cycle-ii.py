#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        s = set()
        while True:
            if not node:
                return None
            if node in s:
                return node
            s.add(node)
            node = node.next
        
# @lc code=end
