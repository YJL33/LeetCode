# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS
# the only logic: return node itself if both node.left and node.right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            # termination:
            if node in (p, q): return node
            
            left = dfs(node.left) if node.left else None
            right = dfs(node.right) if node.right else None
            return node if (left and right) else (left or right)
        
        return dfs(root)
        