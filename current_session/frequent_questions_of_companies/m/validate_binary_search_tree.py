# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checker(root, float('-inf'), float('inf'))
    
    def checker(self, node, lower, upper):
        if not node:
            return True
        if lower < node.val < upper:
            return self.check(node.left, lower, node.val) and self.check(node.right, node.val, upper)
        else:
            return False

# f = TreeNode(6)
a = TreeNode(1)
b = TreeNode(2)
e = TreeNode(5)
d = TreeNode(4, a, e)
c = TreeNode(3, b, d)

p = TreeNode(1)
r = TreeNode(3)
q = TreeNode(2, p, r)
print(Solution().isValidBST(c))
# print(Solution().isValidBST(e))