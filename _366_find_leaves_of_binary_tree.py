"""
 366. Find Leaves of Binary Tree

    Total Accepted: 10016
    Total Submissions: 17631
    Difficulty: Medium
    Contributors: Admin

Given a binary tree, collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree

          1
         / \
        2   3
       / \
      4   5

Returns [4, 5, 3], [2], [1].

Explanation:

1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2

2. Now removing the leaf [2] would result in this tree:

          1

3. Now removing the leaf [1] would result in the empty tree:

          []

Returns [4, 5, 3], [2], [1].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodedct, res = collections.defaultdict(list), []
        self.getLevel(nodedct, root)
        for i in range(len(nodedct)):               # using dictionary to store level-nodes
            res += nodedct[i+1],                    # append them based on levels.
        return res

    def getLevel(self, nodedct, node):              # get each node's level, max(left, right)+1
        if not node: return 0
        l, r = self.getLevel(nodedct, node.left), self.getLevel(nodedct, node.right),
        nodedct[max(l, r)+1] += node.val,
        return max(l, r)+1