# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # check if a is mirror of b
        def checker(a, b):
            if not a and not b: return True
            elif not a or not b: return False
            if a.val != b.val: return False
            return checker(a.left, b.right) and checker(a.right, b.left)
        
        return checker(root.left, root.right)
