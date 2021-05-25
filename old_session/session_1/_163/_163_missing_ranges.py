"""
163. Missing Ranges

    Total Accepted: 16292
    Total Submissions: 53273
    Difficulty: Medium

Given a sorted integer array where the range of elements are [lower, upper] inclusive,
return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
return ["2", "4->49", "51->74", "76->99"].
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower < upper:
                return [str(lower)+"->"+str(upper)]
            elif lower == upper:
                return [str(lower)]
            else:
                return []

        head, tail = 0, len(nums)-1
        while head <= tail and nums[head] < lower:
            head += 1
        while tail >= head and nums[tail] > upper:
            tail -= 1
        if head <= tail:
            return self.generatePair([lower-1] + nums[head:tail+1] + [upper+1])
        else:
            return self.generatePair(nums)

    def generatePair(self, nums):
        pairs = []
        for i in xrange(len(nums)-1):

            if nums[i+1]-nums[i] < 2: continue

            start, end = str(nums[i]+1), str(nums[i+1]-1)

            if nums[i+1]-nums[i] == 2:
                pairs += start,
            else:
                pairs += start+"->"+end,
        return pairs


