"""
424
"""
import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            count[s[j]] += 1
            maxLen = max(maxLen, count[s[j]])
            if j - i + 1 > maxLen + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i