# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import collections
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # craft adjancy list and then use bfs to search the shortest path
        #
        # use a dict to store all its nbs, visit all nodes first to craft the dict
        # key: node, val: list of list [up] [left] [right]
        # nd = collections.defaultdict(list)
        # 
        # tc: O(n) to craft adj list, O(s) (worst case n) for the shortest path
        # sc: O(n) for adj list, O(h) (worst case n) for the height of deque used in bfs
        self.nd = {}

        def addToND(node, parent=None):
            if node.val not in self.nd:
                self.nd[node.val] = [-1, -1, -1]
            if parent:
                self.nd[node.val][0] = parent
            if node.left:
                self.nd[node.val][1] = node.left.val
                addToND(node.left, node.val)
            if node.right:
                self.nd[node.val][2] = node.right.val
                addToND(node.right, node.val)

        addToND(root)
        # print(self.nd)

        dq = collections.deque()
        dq.append(("", startValue))
        
        visited, direction = set(), "ULR"
        visited.add(-1)
        while dq:
            path, val = dq.popleft()
            if val == destValue: return path
            visited.add(val)
            for i in range(3):
                d, node = direction[i], self.nd[val][i]
                if node not in visited:
                    dq.append((path+d, node))
        
        return -1

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
root = TreeNode(5)
f = TreeNode(6)
root.left = a
root.right = b
a.left = c
b.left = f
b.right = d

print(Solution().getDirections(root, 3, 6))