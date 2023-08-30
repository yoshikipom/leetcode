#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tilt_sum = 0
        def dfs(node :TreeNode) -> int:
            nonlocal tilt_sum
            l=0
            r=0
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            tilt_sum += abs(l-r)
            return l+r+node.val
        dfs(root)
        return tilt_sum
            
        
# @lc code=end
