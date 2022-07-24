from typing import List
class Solution:
    # naive approach
    # O(N)*O(t), where t is the operation times, worst case O(N^2)
    def totalSteps_brute(self, nums: List[int]) -> int:
        def helper(arr):
            res = [True for _ in arr]
            res[0] = True
            for i in range(1,len(arr)):
                a = arr[i]
                if a < arr[i-1]:
                    res[i] = False
            return [arr[i] for i in range(len(res)) if res[i]]

        count = 0
        while True:
            output = helper(nums)
            if len(output) == len(nums):
                return count
            nums = output
            count += 1
        
        return -1

    # use monotonic stack
    #
    # think in opposite way, nums[i] can remove all nums[j] s.t. nums[i] > nums[j]
    # count how many elements each one can remove
    #
    # however, if you remove someone, then you shoule either
    # a. replace its position and keep eating (check how many it's eaten), or
    # b. simply +1
    #
    # put (index and count) back to monotonic stack
    # update max_seen
    #
    # tc: O(n) , sc: O(stack), worst case O(n)
    def totalSteps(self, nums: List[int]) -> int:
        ms = []
        max_seen = 0
        for i in range(len(nums)-1, -1, -1):
            n, cnt = nums[i], 0             # cnt: count of nums[i] removes others
            while ms and nums[ms[-1][0]] < n:
                _, prev_cnt = ms.pop()
                cnt = max(cnt+1, prev_cnt)
            max_seen = max(max_seen, cnt)
            ms.append((i, cnt))
        
        return max_seen
    
    # DP
    # 
    # DP[i] is the elements that will be removed by A[i]
    # the element should either keep eating or replace the element that eats something earlier
    # cleaner storage
    # 
    # tc: O(N) sc: O(N)
    def totalSteps_DP(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        res = 0
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[i] > A[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                res = max(res, dp[i])
            stack.append(i)
        return res