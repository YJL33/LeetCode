class Solution:
    def minimumTime(self, s: str) -> int:
        dp, dp2 = [0], [0]
               
        for i in range(len(s)):
            if s[i] == '1':
                dp += min(2+dp[-1], i+1),
            if s[~i] == '1':
                dp2 += min(2+dp2[-1], i+1),
        
        return min(dp[i]+dp2[~i] for i in range(len(dp)))
        