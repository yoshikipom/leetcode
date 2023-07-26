#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
from collections import deque


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        result = None
        tmp = head
        while tmp:
            if tmp.val != val:
                result = tmp
                break
            tmp = tmp.next
        if not result:
            return None
        
        prev_cur = head
        cur = head
        while True:
            cur = cur.next
            if not cur:
                break
            if cur.val != val:
                prev_cur.next = cur
                prev_cur = cur
            else:
                prev_cur.next = None
            
        return result
            
            
        
        
        
# @lc code=end
