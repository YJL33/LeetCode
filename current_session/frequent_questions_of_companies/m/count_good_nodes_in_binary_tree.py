# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        self.helper(root)
        return self.cnt
    
    def helper(self, node, maxSeen=None):
        if not node: return
        if maxSeen is None or node.val >= maxSeen:
            self.cnt += 1

        maxSeen = max(maxSeen, node.val) if maxSeen is not None else node.val
        if node.left:
            self.helper(node.left, maxSeen)
        if node.right:
            self.helper(node.right, maxSeen)
        return
