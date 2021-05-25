"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        nextLayer = []
        if root is not None: nextLayer += root,
        while nextLayer:
            ans += nextLayer[-1].val,
            nodes = []
            for a in nextLayer:
                if a.left is not None:
                    nodes += a.left,
                if a.right is not None:
                    nodes += a.right,
            nextLayer = nodes
        return ans