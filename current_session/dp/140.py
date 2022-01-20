from functools import lru_cache
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # use top-down DP
        res = []
        wSet = set(wordDict)
        @lru_cache(None)
        def dp(start, tmp=""):
            if start == len(s):
                res.append(tmp)
            for end in range(start+1, len(s)+1):
                if s[start:end] in wSet:
                    if tmp != "":
                        dp(end, tmp+" "+s[start:end])
                    else:
                        dp(end, s[start:end])
            return
        dp(0)
        return res