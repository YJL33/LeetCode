"""
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # T:O(n)
        if not nums: return[]

        res = []
        i = 0

        while i < len(nums):
            if i+1 < len(nums) and nums[i+1]-nums[i] == 1:          # if next one is valid
                res.append(str(nums[i]) + '->')                     # we have start and '->'
                i = i+1
                while i+1 <= len(nums) and nums[i]-nums[i-1] == 1:  # find the end
                    i += 1
                res[-1] += str(nums[i-1])                           # we have the end
            else:
                res.append(str(nums[i]))
                i += 1

        return res