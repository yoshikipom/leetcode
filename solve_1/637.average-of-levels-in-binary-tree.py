#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = defaultdict(list)
        
        def dfs(node:TreeNode, level:int):
            nonlocal d
            d[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        
        dfs(root, 0)
        
        result = []
        for k in sorted(list(d.keys())):
            arr = d[k]
            result.append(sum(arr)/len(arr))
            
        return result
            
            
                
        
# @lc code=end
