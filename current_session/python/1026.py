# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0
        if not root: return 0
        def finder(node, max_on_path, min_on_path):
            self.maxDiff = max(self.maxDiff, abs(max_on_path-node.val), abs(node.val-min_on_path))
            max_on_path = max(max_on_path, node.val)
            min_on_path = min(min_on_path, node.val)
            if node.left:
                finder(node.left, max_on_path, min_on_path)
            if node.right:
                finder(node.right, max_on_path, min_on_path)
            return

        finder(root, root.val, root.val)
        return self.maxDiff