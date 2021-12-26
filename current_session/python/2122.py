from typing import List
import collections
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # sum of nums: 2*sum(arr)
        sumOfArr = sum(nums)//2
        lenOfArr = len(nums)//2
        # try to find 2k
        if lenOfArr == 1:
            return [sumOfArr]
        # sort the nums
        # try each K
        # K could come from any an-a0

        def isValidK(twok):
            cnt = collections.Counter(nums)
            res = []
            for n in nums:
                if cnt[n] == 0: continue
                if cnt[n+twok] == 0: return False, []
                cnt[n] -= 1
                cnt[n+twok] -= 1
                res.append(n + twok//2)
            return True, res

        nums.sort()
        for i in range(1,len(nums)):
            twok = nums[i]-nums[0]
            if twok != 0 and twok%2 == 0:
                isValid, res = isValidK(twok)
                if isValid: return res

        return []

print(Solution().recoverArray([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]))