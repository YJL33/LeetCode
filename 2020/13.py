"""
13
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        prev = None
        ans = 0
        for i in range(len(s)):
            cur = mp[s[i]]
            if not prev or cur <= prev:
                ans += cur
                prev = cur
            else:                           # 4 or 9
                ans += cur-2*prev
        
        return ans
