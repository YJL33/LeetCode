"""
see https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""
import collections
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if len(nums) < 2 or max(nums)-min(nums) <= limit: return len(nums)

        # maintain a sliding window (like DP)
        # find the lognest sub array for each r

        l, dp = 0, [0 for _ in nums]
        maxSeen, minSeen = collections.deque(), collections.deque()

        for r in xrange(len(nums)):
            while maxSeen and nums[r] > nums[maxSeen[-1]]:
                maxSeen.pop()
            while minSeen and nums[r] < nums[minSeen[-1]]:
                minSeen.pop()
            maxSeen.append(r)
            minSeen.append(r)

            while nums[maxSeen[0]] - nums[minSeen[0]] > limit:
                l += 1
                while l > minSeen[0]:
                    minSeen.popleft()
                while l > maxSeen[0]:
                    maxSeen.popleft()
            dp[r] = r-l+1

        return max(dp)

print(Solution().longestSubarray([10,1,2,4,7,2],5))
print(Solution().longestSubarray([8,2,4,7],4))
print(Solution().longestSubarray([8],10))
print(Solution().longestSubarray([10,1,2,4,7,2],5))
print(Solution().longestSubarray([4,2,2,2,4,4,2,2],0) == 3)
print(Solution().longestSubarray([4,8,5,1,7,9],6) == 3)
print(Solution().longestSubarray([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39],87) == 25)
