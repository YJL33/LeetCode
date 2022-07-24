from typing import List
class Solution:
    # def combinationSum4(self, nums: List[int], target: int) -> int:
    #     # dp top-down (no memoization)
    #     if target == 0: return 1       
    #     count = 0
    #     for i in range(len(nums)):
    #         if target >= nums[i]:
    #             count += self.combinationSum4(nums, target-nums[i])
    #     return count
    
    def combinationSum4_tablization(self, nums: List[int], target: int) -> int:
        # dp bottom-up
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        nums.sort()
        for k in range(target+1):
            for n in nums:
                if k < n: break
                dp[k] += dp[k-n]                   

        return dp[target]