"""
1239
"""
import collections
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cs = [set()]        # all combinations
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            tmp = []
            for c in cs[:]:
                if a&c: continue
                tmp.append(a|c)
            if len(tmp):
                cs += tmp
        # print(combinations)
        return max([len(x) for x in cs])

print(Solution().maxLength(["un","iq","ue","aa"]))
