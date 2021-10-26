# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # simply use recursive
        def helper(node):
            if not node: return
            node.left, node.right = helper(node.right), helper(node.left)
            return node

        return helper(root)