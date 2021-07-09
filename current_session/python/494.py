"""
494
"""
import collections
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # init
        prevSum = collections.defaultdict(int)
        prevSum[nums[0]] += 1
        prevSum[-1*nums[0]] += 1
        for i in range(1,len(nums)):
            tmp = collections.defaultdict(int)
            for k, v in prevSum.items():
                tmp[k+nums[i]] += v
                tmp[k-nums[i]] += v
            prevSum = tmp
        
        return prevSum[target]

print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1],1),'is 256')