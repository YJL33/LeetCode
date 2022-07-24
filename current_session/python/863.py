"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # craft the adj list
        self.adj = collections.defaultdict(list)
        def helper(node):
            if node.left:
                self.adj[node].append(node.left)
                self.adj[node.left].append(node)
                helper(node.left)
            if node.right:
                self.adj[node].append(node.right)
                self.adj[node.right].append(node)
                helper(node.right)
            return
        helper(root)

        # DFS
        stack = [(target, 0)]
        visited = set()
        res = []
        while stack:
            x, dist = stack.pop()
            visited.add(x)
            if dist == k:
                res.append(x.val)
                continue
            for nb in self.adj[x]:
                if nb not in visited:
                    stack.append((nb, dist+1))
        return res