"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

Accepted 456.9K
Submissions 997.1K
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)

        nums.sort()

        i, res = 0, nums[0]+nums[1]+nums[-1]

        for i in xrange(len(nums)-2):       # leave 2 spots for l and r
        
            if i-1 > 0 and nums[i]==nums[i-1]:  # next distince i
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if abs(target-total) < abs(target-res):
                    res = total
                if total == target:
                    return target
                elif total > target:
                    r -= 1
                else:
                    l += 1

        return res

print Solution().threeSumClosest([-1,2,1,-4], 1)
