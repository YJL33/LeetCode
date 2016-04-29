"""
220. Contains Duplicate III

Given an array of integers,
find out whether there are two distinct indices i and j in the array such that
the difference between nums[i] and nums[j] is at most t and
the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t == 0:
            dic = {}
            for i, v in enumerate(nums):
                if v in dic and i - dic[v] <= k:
                    return True
                dic[v] = i
            return False
        else:
            for i in xrange(len(nums)):
                for j in xrange(i+1, len(nums)):
                    if abs(nums[i]-nums[j]) <= t and abs(i-j) <= k:
                        return True
            return False
