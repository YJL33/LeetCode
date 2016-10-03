"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # To avoid TLE: if invalid in somewhere => whole tree is invalid.
        return self.findDepth(root) != -1

    def findDepth(self, node):
        """
        return the depth of tree using this node as root.
        if node == None:        return 0
        if node has no children:    return 1
        if this tree is not balanced:   return -1
        """
        if not node: return 0                               # this node is Null, return 0
        if node.left or node.right:     # At least one of children isn't None, check the validity
            left_depth = self.findDepth(node.left)
            if left_depth == -1: return -1                  # left tree is invalid, return -1
            right_depth = self.findDepth(node.right)
            if right_depth == -1: return -1                 # right tree is invalid, -1
            if abs(left_depth-right_depth) > 1: return -1   # The difference btw two subtree > 1
            depth = max(left_depth, right_depth) + 1
            return depth                                    # both tree is valid, return the depth
        else:
            return 1                                        # this node has no children, return 1
