"""
437. Path Sum III

    User Tried: 2
    Total Submissions: 2
    Difficulty: Easy

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type s: int
        :rtype: int
        """
        return self.bfs(root, s, [s])

    def bfs(self, node, ori, tgts):
        if not node: return 0
        hit = 0
        for t in tgts:
            if not t-node.val: hit += 1
        tgts = [t-node.val for t in tgts]+[ori]         # update the targets
        return hit+self.bfs(node.left, ori, tgts)+self.bfs(node.right, ori, tgts)