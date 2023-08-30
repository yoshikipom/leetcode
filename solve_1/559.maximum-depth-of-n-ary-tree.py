#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# @lc code=start
"""
# Definition for a Node.
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def dfs(node: Node) -> int:
            depth = 0
            if node.children:
                for child in node.children:
                    depth = max(depth, dfs(child))
            
            return depth + 1
        return dfs(root)
# @lc code=end
