"""
863
"""
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # build connection first
        self.connections = collections.defaultdict(list)
    
        def buildConnection(parent, child):
            self.connections[parent].append(child)
            self.connections[child].append(parent)
            if child.left:
                buildConnection(child, child.left)
            if child.right:
                buildConnection(child, child.right)
            return
        
        buildConnection(None, root)

        # BFS
        stack = [target]
        dist = 0
        visited = set()

        while dist < k:
            tmp = []
            while stack:
                x = stack.pop()
                for n in self.connections[x]:
                    if n not in visited:
                        visited.add(n)
                        tmp.append(n)
            stack = tmp
        return stack

