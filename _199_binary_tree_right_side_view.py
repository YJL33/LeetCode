"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4]. 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Go layer by layer
        res = []
        if root:                                # if root is valid
            level = [root]                      # 1st layer is root
            while level:                        # iterate until there's nothing in next level
                res += level[-1].val,           # add the last seen element in this level
                temp = []
                for node in level:
                    for kid in (node.left, node.right):
                        if kid:
                            temp.append(kid)    # collect elements in next level
                level = temp                    # reset the level as next one
        return res