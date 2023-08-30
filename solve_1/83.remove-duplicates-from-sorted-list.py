#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur:ListNode = head
        while cur and cur.next:
            next_node:ListNode = cur.next
            if next_node.val == cur.val:
                cur.next = next_node.next
            else:
                cur = next_node

        return head
            
# @lc code=end
