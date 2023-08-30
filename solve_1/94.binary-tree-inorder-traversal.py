#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.l = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return self.l
        
        if root.left != None:
            self.inorderTraversal(root.left)
        if root.val != None:
            self.l.append(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)
        return self.l
        
        
        
# @lc code=end
