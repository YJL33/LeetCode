"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        self.getPath(root, '', res)
        return res
    def getPath(self, node, parent_string, res):
        if node is None:
            return
        if parent_string != '':
            current_path = parent_string + '->' + str(node.val)
        else:
            current_path = str(node.val)
        if node.left is None and node.right is None:
            res.append(current_path)
        else:
            self.getPath(node.left, current_path, res)
            self.getPath(node.right, current_path, res)