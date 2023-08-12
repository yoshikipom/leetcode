#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        node: TreeNode = root
        while True:
            if not node:
                break
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            elif val < node.val:
                node = node.left
                
        return None
            
        
# @lc code=end
