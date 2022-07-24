# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import collections
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # keep track the deepest sum
        # level-order traversal
        dq = collections.deque([(root, 0, 0)])
        max_depth, depth_sum = 0, 0
        while dq:
            node, path_sum, lvl = dq.popleft()
            if not node.left and not node.right:
                if lvl == max_depth:
                    depth_sum += node.val
                elif lvl > max_depth:
                    max_depth = lvl
                    depth_sum = node.val
            if node.left:
                dq.append((node.left, path_sum+node.val, lvl+1))
            if node.right:
                dq.append((node.right, path_sum+node.val, lvl+1))
        
        return depth_sum
        