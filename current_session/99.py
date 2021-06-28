"""
99
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Inorder traveral will return values in an increasing order.
        # So if an element is less than its previous element, the previous one should be swapped.
        # O(logn) method
        if not root: return root
        self.inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        if not self.prev:
            self.prev = node
        else:
            if node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
        self.inorder(node.right)

        

