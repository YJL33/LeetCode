"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    def sum_numbers(self, root):
        return self.getSum(root, 0)                         # root has no parent

    def getSum(self, node, parent_val):
        if node is not None:                                # the node is vaild
            current_sum = 10*parent_val+node.val            # the sum = 10*parent_val + node
            if node.left is None and node.right is None:            # Here is leaf!
                return current_sum
            else:                                                   # it's not leaf yet!
                left_sum = self.getSum(node.left, current_sum)
                right_sum = self.getSum(node.right, current_sum)
                return left_sum + right_sum                         # sum up and keep seeking
        else:
            return 0

