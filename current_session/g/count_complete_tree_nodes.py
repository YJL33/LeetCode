# count complete tree nodes
# simply find the last node

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        def findDepth(node):
            if not node: return 0
            return 1+findDepth(node.left)

        leftDepth = findDepth(root.left)
        rightDepth = findDepth(root.right)
        print('h:', leftDepth, rightDepth)

        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

g = TreeNode(7)
f = TreeNode(6)
e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3,f,g)
b = TreeNode(2,d,e)
a = TreeNode(1,b,c)
print(Solution().countNodes(a))