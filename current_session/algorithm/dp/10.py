from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] is the solution of s[:i+1] and p[:j+1]
        # check if p[j] == '*'
        # check if p[j] == '.'
        # check if p[j] == s[i]
        # use DP top-down

        @lru_cache
        def dp(i, j):
            if i == len(s) and j == len(p): return True
            if j == len(p): return False
            
            first = i < len(s) and (p[j] == s[i] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                return (first and dp(i+1, j)) or dp(i, j+2)
            else:
                return first and dp(i+1, j+1)
        
        return dp(0,0)

print(Solution().isMatch("aa", "a"), '== F')
print(Solution().isMatch("aa", "a*"), '== T')
print(Solution().isMatch("ab", ".*"), '== T')
print(Solution().isMatch("aab", "c*a*b"), '== T')
print(Solution().isMatch("a",".*..a*"), '== F')
print(Solution().isMatch("mississippi", "mis*is*p*."), '== F')
print(Solution().isMatch("mississippi", "mis*is*ip*."), '== T')