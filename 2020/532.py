"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""
import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # go through all nums, and add to dict
        # for all n, check if n+k exists or not

        nd = collections.defaultdict(int)
        for n in nums:
            nd[n] += 1

        ans = 0
        vals = nd.keys()

        if k == 0:
            for v in vals:
                if nd[v] > 1:
                    ans += 1
            return ans
        else:
            vals.sort()
            maxVal = vals[-1]
            for v in vals:
                if v > maxVal-k:
                    break
                if v+k in nd:
                    ans += 1
            return ans
