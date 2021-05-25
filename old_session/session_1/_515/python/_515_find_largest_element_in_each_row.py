"""
515. Find Largest Element in Each Row

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

You need to find the largest element in each row of a Binary Tree.

Example:

Input: 

          1
         / \
        2   3
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findValueMostElement(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue, prev = [(0,root)], None
        ans = {}
        while queue:
            level, node = queue.pop(0)
            if level not in ans or node.val > ans[level]:
                ans[level] = node.val
            if node.right:
                queue += (level+1, node.right),
            if node.left:
                queue += (level+1, node.left),
        
        return [ans[i] for i in range(level+1)]