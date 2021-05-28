"""
5
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # use dp
        # dp[i][j] = True if s[i:j] is palindrome
        # note that bool(-1) == True
        dp = [[-1 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        maxLen, start, end = 0, 0, 0
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i > maxLen:
                    # print('True: i, j', i, j, s[i:j+1])
                    maxLen, start, end = j-i, i, j
        
        return s[start:end+1]

print(Solution().longestPalindrome("abcda"), "a")
print(Solution().longestPalindrome("abccba"), "abccba")
print(Solution().longestPalindrome("aaaaaaaaaaa"), "aaaaaaaaaaa")
print(Solution().longestPalindrome("abba"), "abba")
print(Solution().longestPalindrome("ac"), "a")
print(Solution().longestPalindrome(""), "")