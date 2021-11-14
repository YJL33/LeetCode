from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        ans = []
        for i in range(1,len(nums)):
            n = nums[i]             # check each n
            maxSeen = -1
            for j in range(i):
                d = nums[j]         # divisor
                if n%d == 0 and (maxSeen == -1 or len(dp[maxSeen]) < len(dp[j])):
                    maxSeen = j
            if maxSeen >= 0: dp[i] += dp[maxSeen]
            print('dp:', dp)
        
        for s in dp:
            if len(s) > len(ans):
                ans = s
        return ans

print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
print(Solution().largestDivisibleSubset([4,8,10,240]))
print(Solution().largestDivisibleSubset([2,3,4,9,8]))
