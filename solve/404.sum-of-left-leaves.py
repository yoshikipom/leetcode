#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: Optional[TreeNode], is_left: bool):
            nonlocal result

            if not node:
                return
            l: Optional[TreeNode] = node.left
            r: Optional[TreeNode] = node.right
            if is_left and not l and not r:
                result += node.val
                return
            if l:
                dfs(l, True)
            if r:
                dfs(r, False)
                
        dfs(root, False)
        return result
# @lc code=end
