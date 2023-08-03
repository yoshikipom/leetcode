#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        
        stack = []
        stack.append(root)
        while stack:
            node: Node = stack.pop()
            result.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
            
        return result
                
        
# @lc code=end
