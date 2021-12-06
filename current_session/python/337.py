# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def solve(self, root : TreeNode, isParentRobbed : int):
        if root == None:
            return 0
        if root.dp[isParentRobbed] != None:
            return root.dp[isParentRobbed]
        # Parent is robbed so only skip possible
        if isParentRobbed:
            root.dp[isParentRobbed] = self.solve(root.left,0)+self.solve(root.right,0)
        # Parent not robbed so current can be robbed or skipped
        else:
            rob = root.val+self.solve(root.left,1) + self.solve(root.right,1)
            skip = self.solve(root.left,0)+self.solve(root.right,0)
            root.dp[isParentRobbed] = max(skip, rob)
        return root.dp[isParentRobbed]
    
    def fill(self, root : TreeNode):
        if root:
            root.dp = [None, None]
            self.fill(root.left)
            self.fill(root.right)

    def rob(self, root: Optional[TreeNode]) -> int:
        self.fill(root)
        return self.solve(root, 0)