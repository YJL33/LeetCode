# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order: left - root - right
        self.res = []
        def helper(node):
            if not node: return
            if node.left:
                helper(node.left)
            self.res.append(node.val)
            if node.right:
                helper(node.right)
            return
        helper(root)
        return self.res

c = TreeNode(3)
b = TreeNode(2, c, None)
a = TreeNode(1, None, b)

print(Solution().inorderTraversal(a))
