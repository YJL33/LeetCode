"""
see https://leetcode.com/problems/binary-tree-right-side-view/
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
        # similar to bfs
        if not root: return []

        res = []
        stack = [root]

        while stack:
            nextLayer = []
            for nd in stack:
                if nd.left:
                    nextLayer += nd.left,
                if nd.right:
                    nextLayer += nd.right,
            res += stack[-1].val,
            stack = nextLayer

        return res