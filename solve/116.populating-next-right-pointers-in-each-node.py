#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        q = deque()
        q.appendleft((root, 0))
        prev_level = -1
        prev_node = root
        
        while q:
            node:Node
            level:int
            node, level = q.pop()
            
            if not node:
                continue
            # print(node.val, level)
            
            if prev_level != level:
                prev_level = level
            else:
                prev_node.next = node
            prev_node = node
            
            q.appendleft((node.left, level+1))
            q.appendleft((node.right, level+1))
            
        return root
        
# @lc code=end
