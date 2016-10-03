"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        res, temp = [], []
        if root is None:
            return res
        self.findPath(root, target, temp, res)
        return res

    def findPath(self, node, target, current_path_array, output):
        # Main idea: go through layer by layer, pass path array, and check the sum at leaf
        # 1. if this node is valid, add it into current path array
        # 2. if not leaf, pass through the array into its children (separately)
        # 3. if leaf, check the sum of array == target or not
        #       if yes, add this array into output
        #       if not, just forget this array
        if node is None:
            return
        current_path_array.append(node.val)                 # this node is valid, do step 1
        current_sum = target - node.val
        if node.left is not None and node.right is None:    # step 2
            self.findPath(node.left, current_sum, current_path_array, output)
        if node.right is not None and node.left is None:
            self.findPath(node.right, current_sum, current_path_array, output)
        if node.left is not None and node.right is not None:
            current_path_array_2 = []                       # pass the path separately
            for nd in current_path_array:
                current_path_array_2.append(nd)
            self.findPath(node.left, current_sum, current_path_array, output)
            self.findPath(node.right, current_sum, current_path_array_2, output)
        if node.left is None and node.right is None:        # Here's the leaf, do step 3
            if current_sum == 0:
                output.append(current_path_array)

