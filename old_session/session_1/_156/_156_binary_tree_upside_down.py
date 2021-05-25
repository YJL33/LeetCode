"""
 156. Binary Tree Upside Down

    Total Accepted: 16274
    Total Submissions: 39650
    Difficulty: Medium
    Contributors: Admin

Given a binary tree where all the right nodes are either leaf nodes with a sibling
(a left node that shares the same parent node) or empty,

flip it upside down and turn it into a tree
where the original right nodes turned into left leaf nodes.Return the new root.

For example:
Given a binary tree {1,2,3,4,5},

    1
   / \
  2   3
 / \
4   5

return the root of the binary tree [4,5,2,#,#,3,1].

   4
  / \
 5   2
    / \
   3   1  
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        cur, stack = root, []       # stack stores the path to reach new head
        while cur:
            stack += cur,
            cur = cur.left

        cur = stack.pop()
        newroot = cur               # get the new head

        while stack:
            rt = stack.pop()
            cur.right, cur.left = rt, rt.right      # right/left = previous root/previous right
            cur = rt

        cur.right, cur.left = None, None
        return newroot