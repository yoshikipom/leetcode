#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: TreeNode):
            nonlocal result
            l_len = 0
            r_len = 0
            if node.left:
                l_len = dfs(node.left) + 1
            if node.right:
                r_len = dfs(node.right) + 1
            result = max(result, l_len + r_len)
            return max(l_len, r_len)
        dfs(root)
        return result
        
# @lc code=end
