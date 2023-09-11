#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        tmp_head = ListNode()
        tmp_head.next = head
        node: ListNode = tmp_head
        while node:
            arr.append(node)
            node = node.next
        
        if n == 1:
            arr[-2].next = None
        else:    
            arr[-n-1].next = arr[-n+1]

        return tmp_head.next
        
        
# @lc code=end
