# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from functools import cache
from typing import Optional
class Solution:
    # clarfication
    # upper/lowerbound of node.val: 0 <= Node.val <= 10000
    # tree size/height?

    # dp (top-down approach)
    # try rob/not-rob for each node, and compare the result
    # e.g. [3,2,3,null,3,null,1]
    # at root, if we rob we get 3 units, but we cant rob its children, and again we can rob its grant-children
    # if we don't rob at root, then we can(or we can also skip) rob its children, and so on and so forth
    # tc: 
    # O(N) number of nodes in tree
    # sc:
    # O(N), each node we have to store different outcomes of rob/not-rob
    # O(depth of recursive stack)
    def rob_td(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node, canRob):
            if not node: return 0
            res = dp(node.left, True) + dp(node.right, True)    # result of not rob
            if canRob:
                res = max(res, node.val+dp(node.left, False)+dp(node.right, False))
            return res
        
        return dp(root, True)

    # dp (bottom-up approach / iterative implementation)
    # visit all tree and get all nodes with leveling
    # start from leaves, so on and so forth
    # tc:
    # O(N) to visit all node + O(N) to get optimal money
    # sc:
    # O(N) to store all node-leveling + O(N) to store different outcomes
    def rob(self, root: Optional[TreeNode]) -> int:
        # visit every node to get the leveling
        layers = collections.defaultdict(list)
        layers[0] = [root]
        st, lvl = [root], 0
        while st:
            tmp = []
            while st:
                node = st.pop()
                layers[lvl].append(node)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            st, lvl = tmp, lvl+1
        
        outcome = {}
        # now we calculate from leave to root
        # need to store outcome of rob/not-rob, key: node, value: [rob, not-rob]
        for l in range(lvl-1, -1, -1):
            nodes = layers[l]
            for n in nodes:
                rob, notrob = n.val, 0
                if n.left and n.left in outcome:
                    notrob += max(outcome[n.left])
                    rob += outcome[n.left][1]
                if n.right and n.right in outcome :
                    notrob += max(outcome[n.right])
                    rob += outcome[n.right][1]
                outcome[n] = [rob, notrob]

        return max(outcome[root])