
# naive approach
# if the palindrome consists of 'a': change the last element
# else: change first character != 'a'
# O(n)

class Solution:
    def breakPalindrome(self, P: str) -> str:
        if len(P) == 1: return ""
        m, i = len(P)//2, 0
        while i < m and P[i] == 'a':
            i += 1
        if i != m:
            return P[:i]+'a'+P[i+1:]
        return P[:-1]+'b' if P[-1] == 'a' else P[:-1]+'a'

print(Solution().breakPalindrome("aba"))
print(Solution().breakPalindrome("ab"))
print(Solution().breakPalindrome("a"))