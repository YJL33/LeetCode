"""
see https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
class Solution(object):
    def findKthLargest_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]

    def findKthLargest_HP(self, nums, k):
        return heapq.nlargest(k, nums)[-1]