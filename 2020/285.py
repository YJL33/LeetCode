"""
285
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # in-order: left-node-right
        
        def helper(n):
            res = [n]
            if n.left:
                res = helper(n.left)+res
            if n.right:
                res = res+helper(n.right)
            return res

        nodes, nxt = helper(root), None
        
        for i in range(len(nodes)-1, -1, -1):
            if nodes[i] == p:
                return nxt
            nxt = nodes[i]

        return