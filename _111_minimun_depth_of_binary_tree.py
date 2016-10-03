"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is:
the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.getDepth(root, 0, res)         # Use a helper recursive funciton to seek all depth
        if res:
            return min(res)                 # if any valid depth, return the minimum one
        else:
            return 0                        # else, return 0
    def getDepth(self, node, depth, res):
        if node is None:
            return
        elif res and depth+1 >= min(res):   # if current depth is deeper than existing one
            return                          # stop seeking
        elif node.left is None and node.right is None:
            res.append(depth+1)
        else:
            self.getDepth(node.left, depth+1, res)
            self.getDepth(node.right, depth+1, res)