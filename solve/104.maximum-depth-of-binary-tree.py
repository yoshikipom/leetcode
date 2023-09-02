#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def dfs(node: TreeNode, depth: int):
            if not node:
                return
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        return self.max_depth
            
            
        
# @lc code=end
