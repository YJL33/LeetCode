from typing import List
import collections

# use mod
# use partial sum
# from left to right, calculate lsum
# use a dictionary to save all lsums
# key: mod, value: lsums
# if there's a same mod then add x (length of mod value)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        lsum = 0
        ld = collections.defaultdict(list)
        for i in range(len(nums)):
            lsum += nums[i]
            # print("i", i, "nums[i]", nums[i], "lsum", lsum÷, "ld[lsum%k]", ld[lsum%k])
            if (lsum%k) == 0:
                # print("+1")
                res += 1
            if (len(ld[lsum%k]) > 0):
                # print("++", len(ld[nums[i]%k]))
                res += len(ld[lsum%k])
            ld[lsum%k] += i,
            
        return res

print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))