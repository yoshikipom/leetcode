#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        queue = deque()
        max_level = 0
        queue.appendleft((root, 0))
        
        while queue:
            node: TreeNode
            level: int
            node, level = queue.pop()
            if not node:
                continue
            
            d[level].append(node.val)
            max_level = max(max_level, level)
            
            queue.appendleft((node.left, level+1))
            queue.appendleft((node.right, level+1))
        
        result = []
        for level in range(max_level+1):
            result.append(d[level])
        return result
        
        
# @lc code=end
