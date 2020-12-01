"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)

    def check(self, node, lower=-float('inf'), upper=float('inf')):
        if not node:
            return True
        if lower < node.val < upper:
            return self.check(node.left, lower, node.val) and self.check(node.right, node.val, upper)
        else:
            return False
