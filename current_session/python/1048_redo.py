"""
1048
"""
from typing import List
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort by length
        # for each word, check its possible pre-string
        # if exist, add 1
        words.sort(key=len)
        dp = collections.defaultdict(int)
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pre = w[:i]+w[i+1:]
                x = dp[pre]         # zero if not in dp
                dp[w] = max(dp[w], x+1)
        return max(dp.values())

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))