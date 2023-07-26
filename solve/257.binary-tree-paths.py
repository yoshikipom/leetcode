#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        stack = []
        stack.append((root, str(root.val)))
        result = []
        while stack:
            cur, s = stack.pop()
            if not cur.left and not cur.right:
                result.append(s)
                continue
            if cur.left:
                stack.append((cur.left, s + f'->{cur.left.val}'))
            if cur.right:
                stack.append((cur.right, s + f'->{cur.right.val}'))
        return result
        
# @lc code=end
