"""
1448
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # use dfs
        self.count = 0
        
        def dfs(node, maxSeen):
            if not node: return
            if node.val >= maxSeen:     # good
                maxSeen = node.val
                self.count += 1
            dfs(node.right, maxSeen)
            dfs(node.left, maxSeen)
        
        dfs(root, root.val)

        return self.count