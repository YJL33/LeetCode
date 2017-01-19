"""
219. Contains Duplicate II

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False