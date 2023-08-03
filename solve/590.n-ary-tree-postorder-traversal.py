#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        stack.append(root)
        while stack:
            node: Node = stack.pop()
            result.append(node.val)
            for child in node.children:
                stack.append(child)
        return result[::-1]
            
        
# @lc code=end
