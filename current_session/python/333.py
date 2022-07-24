# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        # max seen bst size
        max_seen = 0
        
        # given root_val, left_max, right_min, check validity of BST
        def checker(root_val, left_max, right_min):
            return (root_val > left_max and root_val < right_min)

        # use post-order traversal        
        # we need to know bst-size, max, and min
        def helper(node):
            nonlocal max_seen
            if not node: return [0, float('-inf'), float('inf')]
            l_size, l_max, l_min = helper(node.left)
            r_size, r_max, r_min = helper(node.right)
            if checker(node.val, l_max, r_min):
                max_seen = max(max_seen, l_size+r_size+1)
                return [l_size+r_size+1, max(node.val,r_max), min(node.val,l_min)]
            else:
                return [float('-inf'), float('-inf'), float('inf')]
        
        helper(root)
        
        return max_seen