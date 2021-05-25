"""
102
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack, res = [root], []

        while stack:
            layer = []
            nextLayer = []
            for n in stack:
                layer.append(n.val)
                if n.left is not None:
                    nextLayer.append(n.left)
                if n.right is not None:
                    nextLayer.append(n.right)
            res.append(layer)
            stack = nextLayer

        return res