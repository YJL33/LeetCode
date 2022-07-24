# simply update the longest substr
class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        maxCnt = 0
        cnt = 0
        for i in range(len(s)):
            if not prev or s[i] == prev:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 1
            prev = s[i]

        return max(maxCnt, cnt)

print(Solution().maxPower("tourist"))
print(Solution().maxPower("j"))
print(Solution().maxPower("hooraaaaaaaaaaay"))