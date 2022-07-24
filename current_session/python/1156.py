import collections
import itertools
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # naive approach
        if len(set(text)) == 1: return len(text)
        if len(set(text)) == len(text): return 1        
        char_cnt = collections.Counter(text)
        ans = 0
        def cnt(i,c):
            l, r, cnt = i-1, i+1, 1
            while l >= 0 and text[l] == c: cnt, l = cnt+1, l-1
            while r < len(text) and text[r] == c: cnt, r = cnt+1, r+1
            return min(cnt, char_cnt[c])
        for c in set(text):
            tmp = 0
            # no need to check this one
            if char_cnt[c] == 1 or char_cnt[c] <= ans: continue
            for i,t in enumerate(text):                     # go through the text, O(N)
                if t != c: tmp = max(tmp, cnt(i,c))
            ans = max(tmp, ans)
        
        return ans

    def maxRepOpt1(self, text: str) -> int:
        # use groupby
        # consider 2 cases: extend 1 and replace middle
        if len(set(text)) == 1: return len(text)
        if len(set(text)) == len(text): return 1

        gp = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        char_cnt = collections.Counter(text)

        # extend 1
        res = max(min(k+1, char_cnt[c]) for c, k in gp)

        # replace middle
        for i in range(1, len(gp)-1):
            if gp[i-1][0] == gp[i+1][0] and gp[i][1] == 1:
                res = max(res, min(gp[i-1][1]+gp[i+1][1]+1, char_cnt[gp[i-1][0]]))
        return res

