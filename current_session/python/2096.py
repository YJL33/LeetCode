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
        # use a dict to store all its nbs
        # key: node, val: list of list [up] [left] [right]
        # visit all nodes first
        # nd = collections.defaultdict(list)
        self.nd = {}

        def addToND(node, parentVal=None):
            if node.val not in self.nd:
                self.nd[node.val] = [-1, -1, -1]
            if parentVal:
                self.nd[node.val][0] = parentVal
            if node.left:
                self.nd[node.val][1] = node.left.val
                addToND(node.left, node.val)
            if node.right:
                self.nd[node.val][2] = node.right.val
                addToND(node.right, node.val)

        addToND(root)
        # print(self.nd)

        dq = collections.deque()
        if self.nd[startValue][0] != -1:
            dq.append(('U', self.nd[startValue][0]))
        if self.nd[startValue][1] != -1:
            dq.append(('L', self.nd[startValue][1]))
        if self.nd[startValue][2] != -1:
            dq.append(('R', self.nd[startValue][2]))
        
        visited = set()
        visited.add(startValue)
        while dq:
            path, val = dq.popleft()
            if val == destValue: return path
            visited.add(val)
            up = self.nd[val][0]
            if up not in visited and up != -1:
                dq.append((path+'U', up))
            left = self.nd[val][1]
            if left not in visited and left != -1:
                dq.append((path+'L', left))
            right = self.nd[val][2]
            if right not in visited and right != -1:
                dq.append((path+'R', right))
        
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