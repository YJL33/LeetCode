"""
471
"""
from typing import List
class Solution:
    def encode(self, s: str, memo={}) -> str:
        # 3 options: no encode / encode / split into 2 substring, encode, and combine
        if len(s) <= 4:
            return s
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)                      # if any i, then there's a repeat
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
            memo[s] = min([s, one] + multi, key=len)    # min of 3 options
        return memo[s]

print(Solution().encode("aaa"))
print(Solution().encode("aaaaa"))
print(Solution().encode("aaaaaaaaaa"))
print(Solution().encode("aabcaabcd"))
print(Solution().encode("abbbabbbcabbbabbbc"))
