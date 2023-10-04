#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dummy_head = ListNode(0)
        self.dummy_head.next = head
        
        width = 1
        while True:
            num_loops = self.sub_sort(width)
            
            if num_loops <= 1:
                return self.dummy_head.next
    
            width *= 2
            
    def sub_sort(self, width):
        prev = self.dummy_head
        cur = prev.next
        num_loops = 0
        while cur:
            num_loops += 1
            
            ## generate two list (left, right)
            left_list_tail = None
            right_list_tail = None
            
            left_list = cur
            for _ in range(width):
                if not cur:
                    break
                left_list_tail = cur
                cur = cur.next
            if left_list_tail:
                left_list_tail.next = None
                
            right_list = cur
            for _ in range(width):
                if not cur:
                    break
                right_list_tail = cur
                cur = cur.next
            if right_list_tail:
                right_list_tail.next = None
            
            ## merge two list
            while left_list and right_list:
                if left_list.val <= right_list.val:
                    prev.next = left_list
                    left_list = left_list.next
                else:
                    prev.next = right_list
                    right_list = right_list.next
                prev = prev.next
            
            # handle remainings
            if left_list:
                prev.next = left_list
                prev = left_list_tail
            else:
                prev.next = right_list
                prev = right_list_tail

        return num_loops
            
# @lc code=end
