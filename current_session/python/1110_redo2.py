# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.findNextRoot(root, set(to_delete), True)
        return self.res
    
    # check its children whether it should be removed or not
    def findNextRoot(self, node, toRmv, isRoot=False):
        if not node: return

        l, r = node.left, node.right

        if node.val not in toRmv:
            if isRoot:
                self.res.append(node)
                isRoot = False
            if node.left and node.left.val in toRmv:            # cut its parent
                node.left = None
            if node.right and node.right.val in toRmv:          # cut its parent
                node.right = None
        else:
            node.left, node.right, isRoot = None, None, True    # cut its children
            
        self.findNextRoot(l, toRmv, isRoot)
        self.findNextRoot(r, toRmv, isRoot)
        return