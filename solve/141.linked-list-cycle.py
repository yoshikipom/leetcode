#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur1 = head
        cur2 = head
        while True:
            if not cur2.next or not cur2.next.next:
                return False
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
            
        
        
# @lc code=end
