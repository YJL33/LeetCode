# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # recursively do the problem
        # check if the parent is equal to children or not
        # if so, handle root-left / root-right / left-root-right
        # if not simply check children
        
        self.maxSeen = 0
        if not root: return 0
        
        def helper(node, x):
            if not node: return
            path = 0          
            if node.left and node.left.val == x and node.right and node.right.val == x:
                # make a judgement here
                # path = pick longer one (left or right) => so that the return value can be used
                # update maxSeen with node as bridge of left and right
                l, r = helper(node.left, x), helper(node.right, x)
                self.maxSeen = max(2+l+r, self.maxSeen)
                path = 1+max(l, r)
            elif node.left and node.left.val == x:
                path = 1+helper(node.left, x)
                if node.right: helper(node.right, node.right.val)
            elif node.right and node.right.val == x:
                path = 1+helper(node.right, x)
                if node.left: helper(node.left, node.left.val)
            else:
                if node.left: helper(node.left, node.left.val)
                if node.right: helper(node.right, node.right.val)
            self.maxSeen = max(self.maxSeen, path)
            return path
        
        helper(root, root.val)
        return self.maxSeen