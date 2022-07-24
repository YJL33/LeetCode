from functools import cache

class Solution:
    def canWin(self, s: str) -> bool:
        # flip "++" to "--"
        N = len(s)
        
        # use DP
        # dp(i) is the solution of s[:i]
        # we're only interested in number of consecutive +s
        
        @cache
        def dp(s):
            if len(s) < 2: return False
            if len(s) == 2: return s == '++'
            
            # check all possibilities in between
            for i in range(len(s)):
                if s[i:i+2] == "++" and dp(s[:i]+"-"+s[i+2:]) is False:
                    return True
            
            # no way to win
            return False
            
        return dp(s)