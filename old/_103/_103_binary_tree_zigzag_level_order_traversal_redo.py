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
        res, node, isRev = [], [root], True
        while node:
            temp = []
            if isRev: res += [n.val for n in node],
            else: res += [n.val for n in node[::-1]],
            for n in node:
                for kid in (n.left, n.right):
                    if kid: temp += kid,
            node, isRev = temp, not isRev
        return res
