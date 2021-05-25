"""
513. Find Left Most Element

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Given a binary tree, find the left most element in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree is not NULL.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # implement BFS-like method, in root => right => left order
        if not root: return []
        queue, prev = [root], None
        while queue:
            node = queue.pop(0)
            prev = node
            if node.right:
                queue += node.right,
            if node.left:
                queue += node.left,

        return prev.val
