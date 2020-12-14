"""
https://leetcode.com/problems/delete-nodes-and-return-forest/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)
        ans = []

        def helper(node):
            if node:
                node.right, node.left = helper(node.right), helper(node.left)
                if node.val not in to_delete:
                    return node
                # the following 2 lines is only executed when node in delete list
                ans.append(node.left)
                ans.append(node.right)
        ans.append(helper(root))
        return [a for a in ans if a]
