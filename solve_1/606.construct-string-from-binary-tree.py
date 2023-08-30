#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ''
        def dfs(node: TreeNode):
            nonlocal s
            s += str(node.val)
            if not node.left and not node.right:
                return
            if node.left:
                s += '('
                dfs(node.left)
                s += ')'
            if node.right:
                if not node.left:
                    s += '()'
                s += '('
                dfs(node.right)
                s += ')'

        dfs(root)    
        return s
        
# @lc code=end
