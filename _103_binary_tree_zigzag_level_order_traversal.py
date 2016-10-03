"""
103. Binary Tree Zigzag Level Order Traversal

    Total Accepted: 74137
    Total Submissions: 240362
    Difficulty: Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, nodes, flag = [], [root], False
        while nodes:
            nodes, flag = self.helper(nodes, res, flag), not flag
        return res

    def helper(self, listofnodes, result, rev):
        layer, nextlayer = [], []
        for n in listofnodes[::-1]:
            layer += n.val,
            if rev:
                if n.right: nextlayer += n.right,
                if n.left: nextlayer += n.left,
            else:
                if n.left: nextlayer += n.left,
                if n.right: nextlayer += n.right,
        result += layer,
        return nextlayer

