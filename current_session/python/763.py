"""
see https://leetcode.com/problems/partition-labels/
"""
from typing import List
import collections
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # each letter can only appear in one part
        # as many as possible

        # (naive approach) brute force
        # consider each letter has its own span
        # some are overlapped so they couldn't separate from each other

        # use sliding window
        # first, collect span (occurances)
        # expand r until all elements within won't appear in other places
        # start a new window, so on and so forth 
        # time analysis: O(N) to collect span, O(N) to slide window carefully
        # memory: O(N) for the span information, O(N) for the set used in findR
        
        span = collections.defaultdict(list)
        for i, c in enumerate(s):
            if len(span[c]) == 2:
                span[c].pop()
            span[c].append(i)
               
        def findR(start):
            r = span[s[start]][-1]
            cur = start
            visited = set()
            while cur < r:
                if s[cur] not in visited:
                    r = max(r, span[s[cur]][-1])
                    visited.add(s[cur])
                cur += 1
            return r
        
        res = []
        i = 0
        while i != len(s):
            r = findR(i)
            res.append(r-i+1)           # window size
            i = r+1                     # start a new window
        
        return res


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
