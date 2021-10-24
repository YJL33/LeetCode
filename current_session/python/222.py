# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# keep searching the right node
# if not (then end must happened at the next layer)
# we can do a binary search in the target layer

from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # find the layer
        layer = 1
        node = root
        while node.right:
            node, layer = node.right, layer+1
        
        # now we're at the last complete layer
        # edge case: no next layer
        node, l = root, 1
        while l != layer+1:
            node, l = node.left, l+1
        if not node: return pow(2, layer)-1

        def isValid(x):
            # print('x:',x)
            path, y = [], x
            while y != 1:
                path.append(y%2)
                y = y//2
            n = root
            while n and path:
                d = path.pop()
                n = n.right if d == 1 else n.left
            # print('is valid?', n)
            return n

        l, r = pow(2,layer), pow(2,layer+1)-1
        while l < r:
            m = (l+r)//2
            if isValid(m):
                l = m+1
            else:
                r = m
        
        return l-1