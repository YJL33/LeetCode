"""
14
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a, b = strs[0], strs[-1]
        i = 0
        while i < len(a) and i < len(b):
            if a[i] == b[i]:
                i += 1
            else:
                break
        return a[:i]

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))