"""
see https://leetcode.com/problems/next-permutation/
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return

        # find the largest index such that nums[i] < nums[i+1]
        i = len(nums)-2

        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        # find the largest j such that nums[j] > nums[i]
        # e.g. 1,5,4,3,2
        # i = 0
        # j = 4
        # swap n[i] and n[j] => 2,5,4,3,1
        # organise the rest by reversing
        # 2,5,4,3,1 => 2,1,3,4,5
        else:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1

            # print("i, j", i, j)
            # swap and nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            l, r = i+1, len(nums)-1

            # reverse the rest
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

            return

print Solution().nextPermutation([3,2,1])
print Solution().nextPermutation([1,3,2])
print Solution().nextPermutation([1,1,5])
print Solution().nextPermutation([6,5,4,3,2,1])
print Solution().nextPermutation([4,5,6,3,2,1])