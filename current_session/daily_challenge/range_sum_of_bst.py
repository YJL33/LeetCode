# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # make sure each node is only counted once
        self.rangeSum = 0
        def helper(node):
            if low <= node.val <= high:
                self.rangeSum += node.val
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            return
        helper(root)
        return self.rangeSum