# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.leftLeaves = []
        def helper(node, isLeft):
            if not node.left and not node.right and isLeft:
                self.leftLeaves.append(node.val)
            if node.left:
                helper(node.left, True)
            if node.right:
                helper(node.right, False)
            return
        helper(root, False)
        return sum(self.leftLeaves)