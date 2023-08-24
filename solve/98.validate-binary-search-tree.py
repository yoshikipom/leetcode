#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')
        # if not root:
        #     return True
        
        # acceptable = True
        
        # def dfs(node:TreeNode):
        #     nonlocal acceptable
        #     if not node:
        #         return INF, -INF
        #     l_min, l_max = dfs(node.left)
        #     r_min, r_max = dfs(node.right)
            
        #     if l_max >= node.val or node.val >= r_min:
        #         acceptable = False
            
        #     return min([l_min, node.val, r_min]), max([l_max, node.val, r_max])

        # dfs(root)
        
        # return acceptable
        
        def inorder(node: Optional[TreeNode])->bool:
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.max_val:
                return False
            self.max_val = node.val
            return inorder(node.right)
        
        self.max_val = -INF
        return inorder(root)
            
        
# @lc code=end
