# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.node_sum = 0
        def helper(node, prev):
            if not node.left and not node.right:
                self.node_sum += (2*prev+node.val)
                return
            if node.left:
                helper(node.left, 2*prev+node.val)
            if node.right:
                helper(node.right, 2*prev+node.val)          
            return
        helper(root,0)
        return self.node_sum