#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        l = len(vals)
        # print(vals[:l//2], vals[l-l//2:])
        return vals[:l//2] == vals[l-l//2:][::-1]
            
        
# @lc code=end
