import bisect

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        self.inorder = []
        self.nodeDict = {}

        root = node
        while root.parent:
            root = root.parent

        def helper(nd):
            if nd.left: helper(nd.left)
            self.inorder.append(nd.val)
            self.nodeDict[nd.val] = nd
            if nd.right: helper(nd.right)
            return

        helper(root)
        # print(self.inorder)

        i = bisect.bisect_left(self.inorder, node.val)
        # print('i:', i)

        return self.nodeDict[self.inorder[i+1]] if i+1 < len(self.inorder) else None
