class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        cnt = 0
        maxSeen = cnt
        for c in s:
            if not prev or c != prev:
                cnt = 1
                prev = c
            else:
                cnt += 1
            maxSeen = max(maxSeen, cnt)
        return maxSeen