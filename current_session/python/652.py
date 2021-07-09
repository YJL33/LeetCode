"""
https://leetcode.com/problems/find-duplicate-subtrees/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # simply use a dictionary to see whether the tree exists or not
        # traverse the tree to construct the tree beginning from each root
        def helper(node):
            if node:
                tree = (node.val, helper(node.left), helper(node.right))
                if tree in td:
                    td[tree] += node,
                else:
                    td[tree] = [node]
                return tree
        td = {}
        helper(root)
        ans = []
        keys = td.keys()
        for k in keys:
            if len(td[k]) > 1:
                ans += td[k][0],
        return ans
