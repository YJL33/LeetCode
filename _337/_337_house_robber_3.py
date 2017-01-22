"""
337. House Robber III

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

     3
    / \
   2   3
    \   \
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.toSteal(root))

    def toSteal(self, root):
        # return two values: 'to steal' or 'not to steal'
        if root == None:                                    # Nothing here
            return [0,0]
        if root:
            loot_from_left = self.toSteal(root.left)
            loot_from_right = self.toSteal(root.right)      # iterative here
            # if steal, we can NOT steal connected ones.
            to_steal = root.val + loot_from_left[-1] + loot_from_right[-1]
            # if not_to_steal, we can see whether we're going to steal connected one or not.
            not_to_steal = max(loot_from_left) + max(loot_from_right)
            return [to_steal, not_to_steal]


