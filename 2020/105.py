"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # given preorder and inorder, construct the binary tree
        # preorder: root, left, right
        # inorder: left, root, right

        # use root as mid-point to separate right child and left child
        # e.g.
        # [7, 1,0,3,2,5,4,6, 9,8,10]
        # [0,1,2,3,4,5,6, 7, 8,9,10]

        return self.helper(preorder, inorder)

    def helper(self, parr, iarr):
        if not parr or not iarr: return None

        root = TreeNode(parr[0])
        iPos = iarr.index(root.val)
        root.left = self.helper(parr[1:iPos+1], iarr[:iPos])
        root.right = self.helper(parr[iPos+1:], iarr[iPos+1:])

        return root

