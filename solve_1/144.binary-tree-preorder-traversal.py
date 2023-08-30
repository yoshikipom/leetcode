#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        result = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
            
        return result
            
        
# @lc code=end
