from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use bitmask
        N = len(nums)
        x = 2**N
        res = []
        for i in range(x):              # from 000...000 to 111..111
            tmp = []
            for j in range(N):
                mask = 1<<j
                if mask&i:
                    tmp.append(nums[j])
            res.append(tmp)

        # same, 1 liner
        # res = [ [nums[j] for j in range(N) if i&(1<<j)] for i in range(x) ]
        return res
