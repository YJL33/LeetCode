# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            elif node.left and node.right:
                l, r = helper(node.left), helper(node.right)
                self.res += abs(l-r)
                return node.val+l+r
            elif node.left:
                l = helper(node.left)
                self.res += abs(l)
                return node.val+l
            else:
                r = helper(node.right)
                self.res += abs(r)
                return node.val+r
        
        helper(root)
        
        return self.res