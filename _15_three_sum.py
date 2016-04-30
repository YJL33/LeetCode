"""
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},
A solution set is: (-1, 0, 1), (-1, -1, 2)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        if len(nums) >= 3:
            res = []
            nums.sort()         # Sort the array, O(nlogn)
            max_element = nums[-1]
            for i in xrange(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:  # next distinct i
                    continue
                if (nums[i]+2*max_element < 0):     # i is too small
                    continue
                if (3*nums[i] > 0):                 # i is too large
                    continue
                l, r = i+1, len(nums)-1     # l, r = smallest/biggest one in remaining elements
                while l < r:
                    s = nums[i] + nums[l] + nums[r]     # sum of three elements
                    if s < 0:               # need bigger element
                        l +=1 
                    elif s > 0:             # need smaller element
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])     # A unique triplet
                        while l < r and nums[l] == nums[l+1]:       # move l to r w/o changing value
                            l += 1
                        while l < r and nums[r] == nums[r-1]:       # move r to l w/o changing value
                            r -= 1
                        l += 1; r -= 1              # next distinct l, r
            return res