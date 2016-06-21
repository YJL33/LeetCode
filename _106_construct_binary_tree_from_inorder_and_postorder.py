"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # if the input list are []: return None
        # else:
        # 1. pick root (which is the last one in postorder)
        # 2. use root as mid-point to separate right child and left child
        # 3. deal with right child
        # 4. deal with left child
        def constructor(istart, iend, pstart, pend):
            assert abs(iend-istart) == abs(pend-pstart)
            if iend-istart == 0 or pend-pstart == 0: 
                return None
            root = TreeNode(postorder[pstart:pend][-1])
            # print "root:", root.val, "=>", istart, iend, pstart, pend
            pos = inorder.index(root.val)
            l_pend = pstart + pos - istart
            root.left = constructor(istart,pos,pstart,l_pend)
            root.right = constructor((pos+1),iend,l_pend,(pend-1))
            return root
        
        end = len(inorder)
        res = constructor(0, end, 0, end)

        return res