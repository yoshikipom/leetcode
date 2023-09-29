#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @lc code=start
"""
# Definition for a Node.
"""

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copied_head = Node(head.val)
        
        copied_node: Node = copied_head
        node: Node = head
        d = {}
        d[node] = copied_node
        while node.next:
            next_node = node.next
            copied_next_node = Node(next_node.val)
            
            copied_node.next = copied_next_node
            
            copied_node = copied_node.next
            node = node.next
            d[node] = copied_node
            
        copied_node: Node = copied_head
        node: Node = head
        while node:
            if node.random in d:
                copied_node.random = d[node.random]
            node = node.next
            copied_node = copied_node.next
        
        # print(len(d))
        return copied_head
            
            
        
# @lc code=end
