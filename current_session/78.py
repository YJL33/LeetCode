"""
https://leetcode.com/problems/subsets/
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2**L
        # use binary
        c = 2**len(nums)
        ans = []

        for i in range(c):
            arr, tmp = bin(i)[2:].zfill(len(nums)), []
            for i in range(len(arr)):
                if arr[i] == '1':
                    tmp += nums[i],
            ans += tmp,

        return ans