#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        
        node1 = l1
        node2 = l2
        carry = 0
        cur = root
        while True:
            if not node1 and not node2:
                if carry:
                    cur.next = ListNode(val=1)
                break
            
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            carry, mod = divmod(v1 + v2 + carry, 10)
            new_node = ListNode()
            new_node.val = mod
            cur.next = new_node
            cur = new_node
            
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
            
        
        return root.next

        
# @lc code=end
