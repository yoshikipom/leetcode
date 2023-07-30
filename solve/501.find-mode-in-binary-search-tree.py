#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict, deque
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.



class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = defaultdict(int)
        
        queue = deque()
        queue.append(root)
        while queue:
            node: TreeNode = queue.popleft()
            d[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        m = max(d.values())
        result = []
        for k, v in d.items():
            if m == v:
                result.append(k)
                
        return result
                
            
                
# @lc code=end
