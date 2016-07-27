"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder: Root => Left => Right

        def helper(root, res):
            res += root.val,
            if root.left != None:
                helper(root.left, res)
            if root.right != None:
                helper(root.right, res)
            return


        if root == None:
            return []

        res = []
        helper(root, res)

        return res