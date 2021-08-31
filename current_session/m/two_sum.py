from typing import List
import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = collections.defaultdict(int)
        for i in range(len(nums)):
            n = nums[i]
            if target-n in ndict:
                return [i, ndict[target-n]]
            else:
                ndict[n] = i
        return
