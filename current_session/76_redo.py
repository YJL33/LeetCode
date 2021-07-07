"""
76
"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use sliding window
        # keep increasing r until the criteria is met
        # once the criteria is met we shrink l until the criteria is un-met
        # record start and end

        cnt = collections.Counter(t)

        l, r = 0, 0
        minLen = float('inf')
        res = ""
        while r < len(s):
            if s[r] in cnt:
                cnt[s[r]] -= 1
                while cnt.most_common(1)[0][1] == 0:      # criteria is met
                    if s[l] in cnt: cnt[s[l]] += 1
                    # print('wat now?',cnt)
                    l += 1

                if l-1 >= 0 and s[l-1] in cnt:
                    start, end = l-1, r
                    if end-start < minLen:
                        # print('??', start, end, cnt)
                        res = s[start:end+1]
                        minLen = min(minLen, len(res))
            r += 1
        return res

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("AA", "AA"))
print(Solution().minWindow("A", "AA"))
print(Solution().minWindow("ab","a"))
print(Solution().minWindow("ab","b"))
print(Solution().minWindow("cabwefgewcwaefgcf","cae"),'is cwae')
