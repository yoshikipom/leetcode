#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = root.left
        r = root.right
        
        if not l and not r:
            return True
        if not l and r:
            return False
        if l and not r:
            return False
        
        stack1 = deque()
        stack2 = deque()
        stack1.append(l)
        stack2.append(r)
        while stack1 and stack2:
            cur1 = stack1.pop()
            cur2 = stack2.pop()
            if not cur1 and not cur2:
                continue
            if not cur1 and cur2:
                return False
            if cur1 and not cur2:
                return False
            if cur1.val != cur2.val:
                return False
            print(cur1.val, cur2.val)
            
            stack1.append(cur1.left)
            stack1.append(cur1.right)
            stack2.append(cur2.right)
            stack2.append(cur2.left)
        
            
        return len(stack1) == len(stack2)
        
        
# @lc code=end
