# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        return root if left and right else (left or right)
