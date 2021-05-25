"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def __init__(self):
        self.connection = collections.defaultdict(list)

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        self.dfs(None, root)
        # print(self.connection)

        stack = [target]
        res = [target.val]
        visited = set()
        visited.add(target)
        while K:
            tmp = []
            while stack:
                for x in self.connection[stack.pop()]:
                    if x not in visited:
                        tmp += x,
                        visited.add(x)
            # print tmp
            stack = tmp
            res = [x.val for x in tmp]
            K -= 1
        return res

    def dfs(self, parent, child):
        if parent and child:
            self.connection[parent].append(child)
            self.connection[child].append(parent)
        if child and child.left:
            self.dfs(child, child.left)
        if child and child.right:
            self.dfs(child, child.right)