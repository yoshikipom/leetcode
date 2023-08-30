#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev_node = head
        cur = head.next
        while cur:
            if cur.val != prev_node.val:
                prev_node.next = cur
                prev_node = cur
            else:
                prev_node.next = None
            cur = cur.next
        return head
        
# @lc code=end
