import math
import collections
from typing import List

class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        cnt = 0

        # gcd counter (dict of a, where (a*b)%k == 0)
        # key: gcd of (n, k), value: counts
        ad = collections.Counter()
        
        for i, n in enumerate(nums):
            # use a as pair.second
            a = math.gcd(n, k)

            if a == k:
                # all index before i is valid pair.first
                cnt += i
            else:
                # requires at least b to reach K
                # note that b may not exist in A, but 2b, 3b ... etc may exist
                # TLE if we try all possible b
                # simply try all existing keys in counter in case b is too small
                for b in ad.keys():
                    if (a*b)%k == 0:
                        cnt += ad[b]
            ad[a] += 1
        return cnt