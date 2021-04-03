"""
266
"""
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cd = collections.defaultdict(int)
        for c in s:
            cd[c] += 1
        odd = 0
        for v in cd.values():
            if v%2:
                odd += 1
                if odd > 1:
                    return False
        return True