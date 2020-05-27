"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder: Left => Root => Right

        def helper(root, res):
            if root.left:
                helper(root.left, res)
            res += root.val,
            if root.right:
                helper(root.right, res)
            return


        if not root:
            return []

        res = []
        helper(root, res)

        return res