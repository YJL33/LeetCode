"""
124. Binary Tree Maximum Path Sum

    Total Accepted: 74259
    Total Submissions: 306218
    Difficulty: Hard

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as
any sequence of nodes from some starting node to any node in the tree,
along the parent-child connections.

The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6. 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxVal = -float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum(root)
        return self.maxVal

    def maxSum(self,root):
        """
        :type root:TreeNode
        :rtype :int
        """
        if root == None:
            return 0
        lsum = self.maxSum(root.left)
        rsum = self.maxSum(root.right)
        self.maxVal = max(self.maxVal, root.val+lsum+rsum, root.val+lsum, root.val+rsum, root.val)
        return max(lsum+root.val, rsum+root.val, root.val)
