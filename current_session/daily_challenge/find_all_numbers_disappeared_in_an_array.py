from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [x for x in range(1,len(nums)+1)]
        for n in nums:
            res[n-1] = 0
        return [x for x in res if x != 0]
        