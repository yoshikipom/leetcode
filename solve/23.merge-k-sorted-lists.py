#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
from collections import deque
import heapq
from typing import List, Optional

class Data:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp_head = ListNode()
        node = tmp_head
        queue = []
        for head in lists:
            if not head:
                continue
            heapq.heappush(queue, Data(head.val, head))
        while queue:
            data = heapq.heappop(queue)
            head = data.node
            node.next = ListNode(val=head.val)
            node = node.next
            head = head.next
            if not head:
                continue
            heapq.heappush(queue, Data(head.val, head))
        return tmp_head.next
            
                
        
# @lc code=end
