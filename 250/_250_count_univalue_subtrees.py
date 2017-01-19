"""
 250. Count Univalue Subtrees

    Total Accepted: 11623
    Total Submissions: 29038
    Difficulty: Medium
    Contributors: Admin

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5

return 4.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.isUni(root)
        return self.count

    def isUni(self, node):
        # check whether this node is uni-value subtree or not
        # return the number of uni-value subtrees.
        if not node: return True
        bl, br = self.isUni(node.left), self.isUni(node.right)
        if (bl and br) and (
            not node.left or node.val == node.left.val) and (
            not node.right or node.val == node.right.val):
            self.count += 1
            return True
        else:
            return False
