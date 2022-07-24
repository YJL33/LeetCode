# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # post-order-traverse
        # in each node, check 2 values and update the global max seen:
        # 1. max path sum as a terminal, 2. max path sum as a mid-point
        # return 1 in recursive function
        # tc: O(n)
        # sc: O(1) + O(h), where h is the height of recursion stack
        if not root: return 0
        
        self.maxseen = float('-inf')
        
        def post_order(node):
            if not node: return 0
            lsum = post_order(node.left)
            rsum = post_order(node.right)
            localmax = max(lsum+node.val, rsum+node.val, node.val)           # max path sum as a terminal
            self.maxseen = max(self.maxseen, lsum+rsum+node.val, localmax)
            return localmax
        
        post_order(root)

        return self.maxseen
        

b = TreeNode(2)
c = TreeNode(3)
a = TreeNode(1,b,c)

t = TreeNode(7)
s = TreeNode(15)
r = TreeNode(9)
q = TreeNode(20,s,t)
p = TreeNode(-10,q,r)
print(Solution().maxPathSum(a), "should be 6")
print(Solution().maxPathSum(p), "should be 42")