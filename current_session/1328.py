"""
1328
"""
class Solution:
    def breakPalindrome(self, P: str) -> str:
        if len(P)==1: return ""
        m = len(P)//2
        left = P[:m]
        i = 0
        while i<m and P[i]=='a':
            i += 1
        if i==m:
            if P[-1] == 'a':
                return P[:-1]+'b'
            else:
                return P[:-1]+'a'
        else:
            # print('?',chr(ord(P[i])-1))
            return P[:i]+'a'+P[i+1:]

print(Solution().breakPalindrome("abccba"))
print(Solution().breakPalindrome("a"))
print(Solution().breakPalindrome("aa"))
print(Solution().breakPalindrome("aba"))
