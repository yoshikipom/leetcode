#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.appendleft((root, 1))
        while q:
            cur, depth = q.pop()
            if not cur:
                continue
            if not cur.left and not cur.right:
                return depth
            q.appendleft((cur.left, depth + 1))
            q.appendleft((cur.right, depth + 1))
        
# @lc code=end
