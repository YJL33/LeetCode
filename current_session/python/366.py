# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = -1             # tweak the data structure

from typing import Optional, List

class Solution:

    # 2-pass solution
    # 1. post-order traverse to find the depth of all nodes.
    # 2. fill the result array (implement with pre-order, can use any traverse)
    #
    # if not allowed to tweak the data structure,
    # additional O(n) space for a dictionary (key: node, value: depth) will be needed
    #
    # tc: O(n)
    # sc: O(h), where h is the height of recursion stack
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # tc: O(n)
        # sc: O(h), where h is the height of recursion stack
        def find_depth(node):
            if not node: return
            if not node.left and not node.right:
                node.depth = 0
                return
            find_depth(node.left)
            find_depth(node.right)
            node.depth = 1+max(node.left.depth if node.left else -1, node.right.depth if node.right else -1)
            return

        find_depth(root)
        res = [[] for _ in range(root.depth+1)]
        
        def fill(node):
            if not node: return
            res[node.depth].append(node.val)
            fill(node.left)
            fill(node.right)
            return
        
        fill(root)
        
        return res