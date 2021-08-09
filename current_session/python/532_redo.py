from typing import List
import collections
class Solution:
    def findPairs(self, A: List[int], k: int) -> int:
        numSet = collections.defaultdict(int)
        for a in A:
            numSet[a] += 1
        cnt = 0
        if k != 0:
            for n in numSet:
                if n+k in numSet: cnt += 1
            return cnt
        else:
            for n in numSet:
                if numSet[n] > 1: cnt += 1
            return cnt
        