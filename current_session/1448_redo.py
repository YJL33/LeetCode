"""
1448
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        stack = [(float('-inf'), root)]
        while stack:
            maxSeen, nd = stack.pop()
            if nd.val >= maxSeen:
                maxSeen = max(maxSeen, nd.val)
                cnt += 1
            if nd.left:
                stack.append((maxSeen, nd.left))
            if nd.right:
                stack.append((maxSeen, nd.right))
        return cnt