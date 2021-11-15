# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.inorder = []
        self.nodeDict = {}
        def helper(node):
            if node.left: helper(node.left)
            self.inorder.append(node.val)
            self.nodeDict[node.val] = node
            if node.right: helper(node.right)
            return
        helper(root)
        i = self.inorder.index(p.val)
        return self.nodeDict[self.inorder[i+1]] if i+1 < len(self.inorder) else None
            
