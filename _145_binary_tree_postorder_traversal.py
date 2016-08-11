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
        res = []
        stack = []
        # postorder: left => right => root
        cursor = root
        last_visit = None

        while cursor or stack:              # while cursor/stack are not None/empty
            if cursor:                      # move to left as far as we can
                stack.append(cursor)        # ... add the cursor to stack
                cursor = cursor.left        # ... move to cursor.left
            else:                           # now it's empty
                temp = stack[-1]            # trace back to one lvl higher => temp
                if temp.right and last_visit != temp.right:     # temp.right != None, move to right
                    cursor = temp.right     # ... move to temp.right
                else:                       # temp.right == None, move upward
                    res.append(temp.val)    # ... append the value
                    last_visit = temp       # ... record last visit
                    stack.pop()             # ... remove one from stack

        return res
        