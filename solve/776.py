# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        if root.val <= target:
            sub_left, sub_right = self.splitBST(root.right, target)
            root.right = sub_left
            return root, sub_right
        else:
            sub_left, sub_right = self.splitBST(root.left, target)
            root.left = sub_right
            return sub_left, root
