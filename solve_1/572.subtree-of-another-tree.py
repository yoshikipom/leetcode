#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)
        while stack:
            node: TreeNode = stack.pop()
            if node.val == subRoot.val:
                if is_same(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
                
def is_same(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return is_same(a.left, b.left) and is_same(a.right, b.right)
        
# @lc code=end
