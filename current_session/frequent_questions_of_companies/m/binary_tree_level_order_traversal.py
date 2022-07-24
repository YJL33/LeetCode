# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.res = []

        def helper(A):
            # termination
            if len(A) == 0: return

            # handle the layer
            layer = []
            nextLayer = collections.deque()
            while A:
                x = A.popleft()
                layer.append(x.val)
                if x.left is not None: nextLayer.append(x.left)
                if x.right is not None: nextLayer.append(x.right)
            
            # add the layer into result
            self.res.append(layer)
            if len(nextLayer) != 0: helper(nextLayer)
            return
        
        queue = collections.deque()
        queue.append(root)
        helper(queue)
        return self.res

