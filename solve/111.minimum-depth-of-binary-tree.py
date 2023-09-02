#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
import collections
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.appendleft((root, 1))
        
        while q:
            node, depth = q.pop()
            if not node:
                continue
            if not node.left and not node.right:
                return depth
            q.appendleft((node.left, depth+1))
            q.appendleft((node.right, depth+1))
        raise Exception("result was not found")
        
# @lc code=end
