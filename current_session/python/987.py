"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
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

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # naive approach:
        # step 1. give all nodes x value O(n)
        # step 2. put all nodes into a dictionary, key = x-value, value = node value
        # step 3. get the answer
        self.fillNd(root)
        xs = self.nd.keys()
        xs.sort()
        ans = []
        for x in xs:
            self.nd[x].sort()
            ans += [a[1] for a in self.nd[x]],
        return ans


    def fillNd(self, node, x=0, y=0):
        if not node: return
        self.nd[x].append((y,node.val))
        self.fillNd(node.left,x-1,y+1)
        self.fillNd(node.right,x+1,y+1)
