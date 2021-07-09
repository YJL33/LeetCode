"""
15. 3Sum

Medium

Given an array nums of n integers,
are there elements a, b, c in nums such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Accepted 872.8K
Submissions 3.3M
"""
# import mSort as mSort
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []

        # nums = mSort.mergeSort(nums)
        nums.sort()

        # sort and then move the pointer from smaller side
        # create 2 pointers, check whether their sum == 1st pointer
        # move 1st pointer until it's > 0

        i = 0
        res = []
        # print nums

        while i < len(nums) and nums[i] <= 0:
            if i-1 >= 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            l, r = i+1, len(nums)-1
            print "i, l, r: ", i, l, r
            while l < r:
                print "numbers: ", nums[i], nums[l], nums[r]
                if nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while (l+1 < r and nums[l] == nums[l+1]):
                        l += 1
                    while (r-1 > l and nums[r] == nums[r-1]):
                        r -= 1
                    l, r = l+1, r-1
            i += 1
        return res

print Solution().threeSum([0,0,0,0])
