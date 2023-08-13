# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        
        if root.val <= target:
            sub_left, sub_right = self.splitBST(root.right, target)
            root.right = sub_left
            return root, sub_right
        else:
            sub_left, sub_right = self.splitBST(root.left, target)
            root.left = sub_right
            return sub_left, root
