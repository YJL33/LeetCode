"""
15. 3Sum

    Total Accepted: 181777
    Total Submissions: 862876
    Difficulty: Medium
    Contributors: Admin

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort first. For each element:
        # 1. judge it's validity
        # 2. find existance of other two element s.t. a+b+c == 0

        if len(nums) < 3: return []
        nums.sort()
        res, last = [], len(nums)-1
        for i, a in enumerate(nums):
            if (i > 0 and a == nums[i-1]) or (a + 2*nums[last] < 0) or (3*a > 0):
                continue
            j, k = i+1, last
            while j < k:
                if (a + nums[j] + nums[k] > 0):
                    k -= 1
                elif (a + nums[j] + nums[k] < 0):
                    j += 1
                else:
                    res += [a, nums[j], nums[k]],
                    while (k-1 > j and nums[k-1] == nums[k]):
                        k -= 1
                    while (j+1 < k and nums[j+1] == nums[j]):
                        j += 1
                    j, k = j+1, k-1
        return res

