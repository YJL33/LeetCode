# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # given preorder -> construct the tree and return the root
        # find the right node
        # confine the range of binary search
        # time analysis: 
        # binary search = O(logN), construct one node per search => O(NlogN)
        
        if not preorder: return
        def helper(start, end):
            if start == end or start >= len(preorder): return None
            node = TreeNode(preorder[start])
            mid = bisect.bisect(preorder[start+1:end], node.val)
            node.left = helper(start+1, mid)
            node.right = helper(mid, end)
            return node

        return helper(0, len(preorder))
