#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
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
        seen = set()
        seen_twice = set()
        cur = head
        while cur:
            if cur.val in seen and cur.val not in seen_twice:
                seen_twice.add(cur.val)
            seen.add(cur.val)
            cur = cur.next
        
        tmp_head = ListNode()
        cur = tmp_head
        for num in sorted(list(seen ^ seen_twice)):
            cur.next = ListNode(val=num)
            cur = cur.next
        return tmp_head.next
        
# @lc code=end
