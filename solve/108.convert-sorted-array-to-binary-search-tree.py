#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right) -> TreeNode:
            if not left <= right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)
            return root
            
        return build(0, len(nums)-1)
        
        
# @lc code=end
