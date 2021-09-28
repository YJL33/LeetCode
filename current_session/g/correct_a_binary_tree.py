# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# exactly one error node
import collections
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # find the invalid node first
        # we should be able to get the set of layer while doing BFS
        if root.right == root: return

        dq = collections.deque()
        dq.append(root)
        layer = set()
        layer.add(root)
        invalidNode = None
        parentDict = collections.defaultdict()

        while len(dq) != 0 and invalidNode is None:
            tmp = collections.deque()
            nextLayer = set()
            while len(dq) != 0 and invalidNode is None:
                node = dq.popleft()
                # nextLayer.append(node)
                if node.right:
                    tmp.append(node.right)
                    nextLayer.add(node.right)
                    parentDict[node.right] = node
                if node.left:
                    tmp.append(node.left)
                    nextLayer.add(node.left)
                    parentDict[node.left] = node
                if node.right in layer:
                    invalidNode = node
                    parent = parentDict[invalidNode]
                    if parent.left == invalidNode:
                        parent.left = None
                    elif parent.right == invalidNode:
                        parent.right = None
            dq = tmp
            layer = nextLayer
        
        return root
        


        