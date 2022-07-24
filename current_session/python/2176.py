from typing import List
import collections
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # first, collect all numbers' index
        # i or j must be divisible by k
        # should we only check those index divisible by k(?) => NO (e.g. i=3, j=4, k=6)

        nd = collections.defaultdict(list)
        for i, n in enumerate(nums):
            nd[n].append(i)
        
        cnt = 0
        for _, v in nd.items():
            if len(v) >= 2:
                for j in range(len(v)):
                    for x in range(j+1, len(v)):
                        if (v[j]*v[x])%k == 0:
                            cnt += 1
        return cnt