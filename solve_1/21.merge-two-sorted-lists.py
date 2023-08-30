#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        
        if not node1 and not node2:
            return None
        
        if not node2:
            head = ListNode(val=node1.val)
            node1 = node1.next
        elif not node1:
            head = ListNode(val=node2.val)
            node2 = node2.next
        elif node1.val < node2.val:
            head = ListNode(val=node1.val)
            node1 = node1.next
        else:
            head = ListNode(val=node2.val)
            node2 = node2.next
        current = head
            
        while node1 or node2:
            if not node2:
                current.next = ListNode(val=node1.val)
                node1 = node1.next
            elif not node1:
                current.next = ListNode(val=node2.val)
                node2 = node2.next
            elif node1.val < node2.val:
                current.next = ListNode(val=node1.val)
                node1 = node1.next
            else:
                current.next = ListNode(val=node2.val)
                node2 = node2.next
            current = current.next
        
        return head
                
            
        
        # @lc code=end
