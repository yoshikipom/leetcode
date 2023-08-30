#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
import collections
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        d = collections.defaultdict(lambda: collections.deque())
        max_level = 0
        queue.appendleft((root, 0, True))
        while queue:
            node: TreeNode
            level: int
            left_to_right: bool
            node, level, left_to_right = queue.pop()
            
            if not node:
                continue
            
            if left_to_right:
                d[level].append(node.val)
            else:
                d[level].appendleft(node.val)
            
            max_level = max(max_level, level)
            
            queue.appendleft((node.left, level+1, not left_to_right))
            queue.appendleft((node.right, level+1, not left_to_right))
        
        result = []
        for level in range(max_level+1):
            result.append(list(d[level]))
        # print(result)
        return result
        
# @lc code=end
