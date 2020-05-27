"""
16. 3Sum Closest

Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return 0
        if len(nums) == 3: return sum(nums)
        nums.sort()         # Sort the array, O(nlogn)
        threesum = nums[0] + nums[1] + nums[-1]
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  # next distinct i
                continue
            l = i+1
            r = len(nums)-1     # l, r = smallest/biggest one in remaining elements
            while l < r:
                s = nums[i] + nums[l] + nums[r] # sum of three elements
                if abs(s-target) < abs(threesum-target):
                    threesum = s            # Update the answer
                if s == target:             # (Putting it here would be faster.)
                    return target           # exactly get the target!
                elif s < target:            # need bigger element
                    l +=1
                elif s > target:            # need smaller element
                    r -= 1
        return threesum