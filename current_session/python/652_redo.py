# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
import collections
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        # use dict
        # key=tree, val=list of nodes
        treeDict = collections.defaultdict(list)

        def helper(node):
            res = ""
            if node:
                # serialize the tree, pre-order
                res += str(node.val) + "."
                res += helper(node.left) + "."
                res += helper(node.right)
            else:
                res += "#"
            
            treeDict[res].append(node)
            return res

        helper(root)
        # print('treeDict:', treeDict)

        ans = []
        for _, v in treeDict.items():
            if len(v) > 1 and v[0] is not None:
                ans.append(v[0])
        return ans