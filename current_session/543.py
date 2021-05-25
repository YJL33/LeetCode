"""
543
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        # for each node, the diameter is the sum of maxDepth of both children

        def getMaxDepth(node):      # dfs
            if not node:
                return 0
            left, right = getMaxDepth(node.left), getMaxDepth(node.right)
            self.ans = max(self.ans, left+right)        # update the answer here
            return max(left, right)+1                   # return the depth
        
        getMaxDepth(root)
        return self.ans