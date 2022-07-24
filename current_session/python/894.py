# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import cache
from typing import List, Optional
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # clarification
        # restrictions on memory usage? timeout? (e.g. plain Node ~28bytes)
        # 
        # ideas
        # consider number of left-child-bst * right-child-bst
        # we should have fixed number of possibilies
        # numbers that can make binary tree: 1, 3...
        # binary trees: each node has exactly 0 or 2 children
        
        @cache
        def helper(x):
            # given number x, use 1 as root, say left bst has L possibilities, and right bst has R possibilities
            # we have L+R+1
            # calculate sum of l*r for all L and R 
            
            if x == 1: return [TreeNode(0)]
            if x == 2: return None
            
            ans = []
            for i in range(x):
                lefts, rights = helper(i), helper(x-1-i)
                if lefts and rights:
                    for l in lefts:
                        for r in rights:
                            rt = TreeNode(0)
                            rt.left, rt.right = l, r
                            ans.append(rt)
            return ans
        
        return helper(n)