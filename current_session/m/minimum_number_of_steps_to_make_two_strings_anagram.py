# size is the same
import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1, cnt2 = collections.Counter(s), collections.Counter(t)
        for k, v in cnt1.items():
            while v:
                if k in cnt2 and cnt2[k] > 0:
                    cnt2[k] -= 1
                v -= 1
        # print(cnt1, cnt2)
        return sum([x for x in cnt2.values()])

print(Solution().minSteps("bab", "aba"))
print(Solution().minSteps("leetcode", "practice"))
print(Solution().minSteps("anagram","mangaar"))
print(Solution().minSteps("xxyyzz", "xxyyzz"))
print(Solution().minSteps("gctcxyuluxjuxnsvmomavutrrfb","qijrjrhqqjxjtprybrzpyfyqtzf"))