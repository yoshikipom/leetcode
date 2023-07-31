#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(node: TreeNode):
            bisect.insort(arr, node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        result = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            result = min(result, arr[i+1]-arr[i])
        return result
            
            
        
# @lc code=end
