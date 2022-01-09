from typing import List
import collections
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # see if opposite exists
        # if w[0] == w[1], can act as center, but can also put them twice
        # assume including only unique word in words
        c1 = collections.Counter(words)
        c2 = collections.Counter([w[::-1] for w in words])
        s1 = set([w for w in c1.keys()])
        s2 = set([w for w in c2.keys()])
        s = s1.intersection(s2)
        print('s', [(k, c1[k]) for k in s])
        L = 0
        used = set()
        has_center = False
        for w in s:
            if w not in used:
                if w != w[::-1]:
                    L += min(c1[w], c1[w[::-1]])*4
                    used.add(w[::-1])
                else:
                    if not has_center:
                        L += c1[w]*2
                        if c1[w]%2: has_center = True
                    else:
                        L += (c1[w]-c1[w]%2)*2
        return L

print(Solution().longestPalindrome(["mm","mm","yb","by","bb","bm","ym","mb","yb","by","mb","mb","bb","yb","by","bb","yb","my","mb","ym"]), '30')