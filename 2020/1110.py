"""
see https://leetcode.com/problems/delete-nodes-and-return-forest/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.output = []
        self.toRemove = []
        self.removeDict = {}

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """

        # visit all nodes and remove targets.
        # keep an output array which stores all remaining roots
        # if node.val == target, add node.left and node.right into output

        for n in to_delete:
            self.removeDict[n] = True

        output, stack = {}, [(root, None, None)]
        i = 0

        while stack:
            nd, pr, isLeft = stack.pop()
            self.helper(nd, pr, isLeft)
            if nd.left:
                stack += (nd.left, nd, True),
            if nd.right:
                stack += (nd.right, nd, False),

        self.remove()

        return self.output
    
    # prepare to do 2 things:
    # a. if it's in removal list, remove itself in the tree -> inform its parent
    # b. add its two children into output, if they're not in removal list
    def helper(self, nd, parent, isLeft):
        if parent is None and nd.val not in self.removeDict:
            self.output += nd,
        if nd.val in self.removeDict:
            if isLeft is not None:
                self.toRemove += (parent, isLeft),
            if nd.left and nd.left.val not in self.removeDict:
                self.output += nd.left,
            if nd.right and nd.right.val not in self.removeDict:
                self.output += nd.right,

    def remove(self):
        for n in self.toRemove:
            if n[1]:
                n[0].left = None
            else:
                n[0].right = None

