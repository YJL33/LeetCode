"""
226
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def helper(node):
            if not node: return
            node.right, node.left = helper(node.left), helper(node.right)
            return node

        helper(root)
        return root