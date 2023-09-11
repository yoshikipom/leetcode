#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False

        def dfs(node: TreeNode, sum:int):
            if not node:
                return
            if not node.left and not node.right and sum+node.val == targetSum:
                self.result = True
            dfs(node.left, sum+node.val)
            dfs(node.right, sum+node.val)
        dfs(root, 0)
        return self.result
                
                
        
# @lc code=end
