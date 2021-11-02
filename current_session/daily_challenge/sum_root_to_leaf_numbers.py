# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # get all 'root-to-leaf' numbers and sum them together
        rootToLeafNumbers = []

        def getAllNumbers(node, carry=0):
            if not node.left and not node.right:    # leaf
                rootToLeafNumbers.append(10*carry+node.val)
            if node.left:
                getAllNumbers(node.left, 10*carry+node.val)
            if node.right:
                getAllNumbers(node.right, 10*carry+node.val)
            return

        getAllNumbers(root)

        return sum(rootToLeafNumbers)
