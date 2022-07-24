from functools import lru_cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # top-down DP
        @lru_cache(None)
        def dp(l, r, k):
            if k >= r-l+1: return True
            if l >= r: return True
            if s[l] == s[r]:
                return dp(l+1, r-1, k)
            else:
                if k == 0: return False
                return dp(l+1, r, k-1) or dp(l, r-1, k-1)
        
        dp.cache_clear()
        return dp(0, len(s)-1, k)

print(Solution().isValidPalindrome("abcdeca", 2))
print(Solution().isValidPalindrome("abbababa", 1))
print(Solution().isValidPalindrome("cabbabbad", 1))
print(Solution().isValidPalindrome("cabbabbad", 2))
print(Solution().isValidPalindrome("ccabbabbadd", 2))