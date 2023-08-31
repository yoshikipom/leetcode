#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node:Optional[ListNode] = head
        prev = None
        while node:
            next_tmp = node.next
            node.next = prev
            prev = node
            node = next_tmp
        return prev
        
# @lc code=end
