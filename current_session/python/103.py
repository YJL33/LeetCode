"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def __init__(self):
        self.nd = collections.defaultdict(list)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # naive approach:
        # go through all nodes and number their layer
        self.fillND(root)
        layers = self.nd.keys()
        layers.sort()
        ans = []
        for l in layers:
            # if l%2:
            ans.append(self.nd[l][::-1 if l%2 else 1])
            # else:
                # ans.append(self.nd[l])
        return ans

    def fillND(self, node, layer=0):
        if not node: return
        self.nd[layer].append(node.val)
        self.fillND(node.left, layer+1)
        self.fillND(node.right, layer+1)
