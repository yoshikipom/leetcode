#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)
        
        l = 0
        r = len(values) - 1
        
        # print(values)
        
        while l < r:
            total = values[l] + values[r]
            if total < k:
                l += 1        
            elif total == k:
                return True
            elif k < total:
                r -= 1
        return False
        
# @lc code=end
