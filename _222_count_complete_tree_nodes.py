"""
 222. Count Complete Tree Nodes

    Total Accepted: 46830
    Total Submissions: 175973
    Difficulty: Medium
    Contributors: Admin

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def countNodes1(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # TLE
    #     if not root: return 0
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # check the length (go directly to the most left) of left node and right node
        # if same => left subtree is full
        # else => right subtree is full.
        if not root: return 0
        leftDepth, rightDepth = self.getDepth(root.left), self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root: return 0
        else: return 1 + self.getDepth(root.left)