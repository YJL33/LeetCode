"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if the input list are []: return None
        # else:
        # 1. pick root (which is the first one in preorder)
        # 2. use root as mid-point to separate right child and left child
        # 3. deal with right child
        # 4. deal with left child
        #[7, 1,0,3,2,5,4,6, 9,8,10]
        #[0,1,2,3,4,5,6, 7, 8,9,10]
        def constructor(istart, iend, pstart, pend):
            assert abs(iend-istart) == abs(pend-pstart)
            if iend-istart == 0 or pend-pstart == 0: 
                return None
            root = TreeNode(preorder[pstart:pend][0])
            # print "root:", root.val, "=>", istart, iend, pstart, pend
            pos = inorder.index(root.val)
            l_pend = pstart + pos - istart
            root.left = constructor(istart,pos,pstart+1,l_pend+1)
            root.right = constructor((pos+1),iend,l_pend+1,pend)
            return root
        
        end = len(inorder)
        res = constructor(0, end, 0, end)

        return res