"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree,
each node's right child points to the next node of a pre-order traversal.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        res = []
        self.getOrder(root, res)            # 1st step: get the order of all nodes.
        # print res
        self.assignNodes(root, res)         # 2nd step: assign all nodes.

    def getOrder(self, node, order_list):
        if node is None:
            return
        else:
            order_list.append(node)
        if node.left is not None:
            self.getOrder(node.left, order_list)
        if node.right is not None:
            self.getOrder(node.right, order_list)

    def assignNodes(self, node, order_list):
        if node is None:
            return
        for i in xrange(len(order_list)-1):
            order_list[i].left = None
            order_list[i].right = order_list[i+1]



