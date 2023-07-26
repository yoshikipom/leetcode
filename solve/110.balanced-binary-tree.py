#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node: TreeNode) -> Tuple[bool, int]:
        if not node:
            return True, -1
        l_balanced, l_height = self.helper(node.left)
        if not l_balanced:
            return False, 0
        
        r_balanced, r_height = self.helper(node.right)
        if not r_balanced:
            return False, 0
        
        return (abs(l_height - r_height) < 2), 1 + max(l_height, r_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

# @lc code=end
