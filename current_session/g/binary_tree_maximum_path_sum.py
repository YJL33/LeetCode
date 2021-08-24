# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use dfs(?)
# path = node+maxPath(Left)+maxPath(Right)

from typing import Optional
class Solution:
    mx = -1*float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root)
        return self.mx
    
    def maxPath(self, node) -> int:
        if node is None: return 0
        x, lx, rx = node.val, self.maxPath(node.left), self.maxPath(node.right)
        self.mx = max(self.mx, x, x+lx+rx, x+lx, x+rx)      # update global 2 way path sum
        return max(x, x+rx, x+lx)                           # one way path

b = TreeNode(2)
c = TreeNode(3)
a = TreeNode(1,b,c)

t = TreeNode(7)
s = TreeNode(15)
r = TreeNode(9)
q = TreeNode(20,s,t)
p = TreeNode(-10,q,r)
print(Solution().maxPathSum(a), "should be 6")
print(Solution().maxPathSum(p), "should be 42")