# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return
        if len(nums) == 1: return TreeNode(nums[0])
        L = len(nums)
        mid = TreeNode(nums[L//2])
        mid.left, mid.right = self.sortedArrayToBST(nums[:L//2]), self.sortedArrayToBST(nums[(L//2)+1:])
        return mid

# print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
x = Solution().sortedArrayToBST([-10,-3,0,5,9])
# print(x.left.left.val, x.left.val, x.val, x.right.val, x.right.left.val)
print(Solution().sortedArrayToBST([1,3]))