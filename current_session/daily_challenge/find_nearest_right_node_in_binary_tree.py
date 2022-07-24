# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        # use BFS-like strategy: craft layer(s)
        dq = collections.deque()
        dq.append((root,0))
        while dq:
            while len(dq) != 0:
                nd, layer = dq.popleft()
                if nd == u:
                    return dq.popleft()[0] if dq and dq[0][1] == layer else None
                if nd.left:
                    dq.append((nd.left, layer+1))
                if nd.right:
                    dq.append((nd.right, layer+1))
        return None