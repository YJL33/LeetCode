"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # see https://en.wikipedia.org/wiki/File:LISDemo.gif
        if not nums: return 0

        res = []

        for n in nums:
            x = bisect.bisect_left(res, n)
            if x >= len(res):
                res += n,
            else:
                res[x] = n

        return len(res)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))