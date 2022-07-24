from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # clarification
        #
        # largest divisible subset (aka lds)
        # is the given num sorted?
        # e.g. [1,2,4,8]
        # e.g. [1,3,9,27,54]
        #
        # idea: bottom up dp
        # 1. sort the array
        # 2. dp = [[n] for n in nums], which is the initial state of dp, the lds is itself
        # 3. for n in nums, check all previous i s.t. i < n, if n%i == 0, add it into the largets divisible set
        # so on and so forth
        #
        # e.g. [1,3,9,27,54,81,243]
        #       [1], [1,3], [1,3,9], [1,3,8,27],  [1,3,9,27,54], [1,3,9,27,81], [1,3,9,27,81,243]
        #
        # tc: O(n^2)
        # sc: O(n*lds of each n), worst case ~O(n*(n-1)/2)
        nums.sort()
        dp = [[n] for n in nums]
              
        for i,n in enumerate(nums):
            maxSeen = -1
            for j,d in enumerate(nums[:i]):     # divisor
                if n%d == 0 and (maxSeen == -1 or len(dp[maxSeen]) < len(dp[j])):
                    maxSeen = j
            if maxSeen >= 0: dp[i] += dp[maxSeen]
            # print('dp:', dp)
        
        ans = []
        for s in dp:
            if len(s) > len(ans):
                ans = s
        return ans