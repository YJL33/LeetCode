# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
# find the array first O(n)
# recursion => O(NlogN)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return

        def findMaxIndex(A):
            maxIndex = -1
            for i in range(len(A)):
                if maxIndex == -1 or A[i] >= A[maxIndex]:
                    maxIndex = i
            return maxIndex

        i = findMaxIndex(nums)
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root

        