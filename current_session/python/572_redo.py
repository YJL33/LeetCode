# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find all candidates that has same value as the subroot in first root
        val = subRoot.val
        candidates = []
        def finder(node, val):
            if node is None: return None
            if node.val == val: candidates.append(node)
            return finder(node.left, val) or finder(node.right, val)

        finder(root, val)

        # compare both three
        def compare(a, b):
            if a is None and b is None: return True
            elif a is None or b is None: return False
            elif a.val != b.val: return False
            return compare(a.left, b.left) and compare(a.right, b.right)
        
        return any([compare(a, subRoot) for a in candidates])