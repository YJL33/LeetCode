# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
import collections

class Solution:
    def findLeaves_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursive
        res = []
        def helper(node, leaves, parent=None):   # remove leave and put it into result
            if not node.left and not node.right:
                leaves.append(node.val)
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
                return
            if node.left:
                helper(node.left, leaves, node)
            if node.right:
                helper(node.right, leaves, node)
            return

        dh = TreeNode(0)
        dh.left = root
        while dh.left:
            leaves = []
            helper(root, leaves, dh)
            res.append(leaves)
        return res

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n)
        self.nodeDict = collections.defaultdict(list)
        def mark(node):
            if not node.left and node.right:
                self.nodeDict[0].append(node)
                return 1
            vals = []
            if node.left:
                vals.append(mark(node.left))
            if node.right:
                vals.append(mark(node.right))
            val = 1+max(vals)
            self.nodeDict[val].append(node)
            return val

        mark(root)
        keys = [k for k in self.nodeDict.keys()]
        keys.sort()
        res = []
        for k in keys:
            res.append(self.nodeDict[k])
        return res