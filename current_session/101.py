# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(l, r):
            if not r and l: return False
            if not l and r: return False
            if not l and not r: return True
            if r.val != l.val: return False
            return helper(r.left, l.right) and helper(r.right, l.left)
        return helper(root.left, root.right)