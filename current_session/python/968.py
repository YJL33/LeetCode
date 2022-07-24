# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        
        # define the return states, and use a global counter to add 1 when setup a camera
        # 0: should be covered by parent
        # 1: should setup a camera
        # 2: should be covered by children
        def dfs(node):
            if not node: return 2               # should tell parent that i'm fine but you should take care your self
            if not node.left and not node.right:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if (l==0) or (r==0):
                self.cnt += 1
                return 1
            if (l==1) or (r==1):
                return 2
            return 0                            # should tell parent that i'm not covered at all, pls setup one
            
        initial = dfs(root)
        return (1 if initial == 0 else 0) + self.cnt