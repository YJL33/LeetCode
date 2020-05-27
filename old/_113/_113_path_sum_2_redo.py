"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        # Use stack: add each path's sum and it's last element into stack.
        # if meet leave: check whether valid or not.
        if not root: return []

        stack, res = [[root]], []     # stack: a list of nodes
        while stack:
            path = stack.pop()
            if not path[-1].left and not path[-1].right:
                if target == sum([n.val for n in path]):
                    res.append([n.val for n in path])
            if path[-1].left:
                stack += path+[path[-1].left],
            if path[-1].right:
                stack += path+[path[-1].right],

        return res