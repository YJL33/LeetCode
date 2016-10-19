"""
 99. Recover Binary Search Tree

    Total Accepted: 61507
    Total Submissions: 218764
    Difficulty: Hard
    Contributors: Admin

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
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