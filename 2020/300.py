"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # see https://en.wikipedia.org/wiki/File:LISDemo.gif
        if not nums: return 0

        res = [[nums[0]]]

        for n in nums[1:]:
            sa = len(res)-1
            if n > res[-1][-1]:
                tmp = res[-1]+[n]
                # print('tmp:',tmp)
                res.append(tmp)
            # find the subArr to update
            # here we can change into binary search
            while n <= res[sa][-1] and sa >= 0:
                sa -= 1
            res[sa+1][-1] = n
            # print(res)

        return len(res[-1])

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))