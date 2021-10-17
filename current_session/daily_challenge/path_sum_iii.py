# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import collections
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0

        # DFS go through whole tree, carry the previous path sum
        # if meet targetSum: add one
        def dfs(node, prevSums):
            if not node: return
            # print("node:", node.val, "prevSums:", prevSums)
            if len(prevSums) > 0:
                # key: sum, val: cnt
                tmp = collections.defaultdict(int)
                for k, v in prevSums.items():
                    if k+node.val == targetSum:
                        self.cnt += v
                    tmp[k+node.val] += v
                prevSums = tmp

            if node.val == targetSum:
                self.cnt += 1
            prevSums[node.val] += 1
            
            dfs(node.left, prevSums)
            dfs(node.right, prevSums)
            return
        
        dct = collections.defaultdict(int)
        dfs(root, dct)
        return self.cnt