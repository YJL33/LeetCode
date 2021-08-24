import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # go through t
        # or we just use something like (need x)
        # use sliding window, if still need something, inrease r
        # if satisfied, increase l until one missing

        self.cnt = collections.Counter(t)

        l, r = 0, 0
        minLen = float('inf')
        res = ""
        while r < len(s):
            r = self.findR(r, s)
            l = self.findL(l, s)
            # print('l, r', l, r, minLen)

            if l-1 >= 0 and s[l-1] in self.cnt:
                start, end = l-1, r
                if end-start < minLen:
                    # print('??', start, end, cnt)
                    res = s[start:end]
                    minLen = min(minLen, len(res))
        return res
    
    def findR(self, r, s):
        while r < len(s) and self.cnt.most_common(1)[0][1] != 0:
            if s[r] in self.cnt: self.cnt[s[r]] -= 1
            r += 1
        return r
    
    def findL(self, l, s):
        while self.cnt.most_common(1)[0][1] == 0:      # criteria is met
            if s[l] in self.cnt: self.cnt[s[l]] += 1
            l += 1
        return l


print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution().minWindow(s = "AA", t = "AA"))
print(Solution().minWindow(s = "ab", t = "a"))
print(Solution().minWindow("ab","b"))
print(Solution().minWindow("cabwefgewcwaefgcf","cae"),'is cwae')