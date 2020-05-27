"""
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's
(binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def node(val, left, right):         # Node constructor
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)    # for loop with 3 args
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]     # invalid nodes return as None
        if n == 0:
            return []
        else:
            return trees(1, n)