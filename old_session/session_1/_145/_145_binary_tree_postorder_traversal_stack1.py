"""
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # do it iteratively with stack (first in last out), T: O(n), S: O(n)
        if not root: return []
        cursor, res, stack, prev = root, [], [], None
        while cursor or stack:
            if cursor:
                stack += cursor,                # add root into stack
                cursor = cursor.left
            else:                               # no more lefts, check its counterpart
                tmp = stack[-1]
                if tmp.right and prev != tmp.right:         # counterpart exists
                    cursor = tmp.right
                else:                           # counterpart also not existing
                    prev = tmp                  # no moving, just staying here
                    res += stack.pop().val,
        return res
