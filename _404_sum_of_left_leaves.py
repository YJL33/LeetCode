"""
404. Sum of Left Leaves

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, node):
        if node == None:
            return 0
        if node.left and not node.left.left and not node.left.right:  # a left leave
            return node.left.val+self.helper(node.right)
        else:
            return self.helper(node.left)+self.helper(node.right)
