#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = -float('inf')
        self.result = float('inf')
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            self.result = min(self.result, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.result
            
        
# @lc code=end
