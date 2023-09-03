#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return None
            elif not node1 and node2:
                return node2
            elif node1 and not node2:
                return node1
            else:
                node1.left = dfs(node1.left, node2.left)
                node1.right = dfs(node1.right, node2.right)
                node1.val += node2.val
                return node1
            
        return dfs(root1, root2)
        
# @lc code=end
