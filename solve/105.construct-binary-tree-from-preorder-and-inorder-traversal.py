#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def arr_to_tree(left, right) -> TreeNode:
            nonlocal preorder_cur
            
            if not left <= right:
                return None
            
            preorder_root_val = preorder[preorder_cur]
            root = TreeNode(val=preorder_root_val)
            preorder_cur+=1
            
            inorder_root_index = inorder_map[preorder_root_val]
            root.left = arr_to_tree(left, inorder_root_index-1)
            root.right = arr_to_tree(inorder_root_index+1, right)
            return root
        
        preorder_cur = 0
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        return arr_to_tree(0, len(preorder)-1)
        
# @lc code=end
