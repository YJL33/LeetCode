# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import collections
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # find the depth of target node
        # BFS
        def findDepth(target):
            dq = collections.deque()
            dq.append((root, None, 1))
            while len(dq) > 0:
                node, parent, depth = dq.popleft()
                if node.val == target:
                    return (parent, depth)
                if node.left: dq.append((node.left, node, depth+1))
                if node.right: dq.append((node.right, node, depth+1))
            return (None, -1)
        
        a, b = findDepth(x), findDepth(y)
        return a[1] == b[1] and a[0] != b[0]
