"""
 104. Maximum Depth of Binary Tree

    Total Accepted: 212597
    Total Submissions: 415724
    Difficulty: Easy
    Contributors: Admin

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path,
from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # use BFS
        if not root: return 0
        queue, res = [(1, root)], 1
        while queue:
            depth, node = queue.pop(0)
            if depth > res:
                res = depth
            if node.left:
                queue += (depth+1, node.left),
            if node.right:
                queue += (depth+1, node.right),
        return res
