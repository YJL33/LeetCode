"""
1395
"""
from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(len(rating)):
            llc, lgc, rlc, rgc = 0, 0, 0, 0
            # optimization: binary search
            for x in rating[:i]:
                if x < rating[i]:
                    llc += 1
                elif x > rating[i]:
                    lgc += 1
            for y in rating[i+1:]:
                if y < rating[i]:
                    rlc += 1
                elif y > rating[i]:
                    rgc += 1
            cnt += llc*rgc + lgc*rlc
        return cnt