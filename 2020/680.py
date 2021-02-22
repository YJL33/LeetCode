'''
680
'''
class Solution:
    def validPalindrome(self, s: str, skip: bool=False) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l, r = l+1, r-1
            else:
                if skip:
                    return False
                else:
                    # either delete s[r] or s[l]
                    return self.validPalindrome(s[l:r], True) or self.validPalindrome(s[l+1:r+1], True)
        return True

print(Solution().validPalindrome('aba'))
print(Solution().validPalindrome('abba'))
print(Solution().validPalindrome('abca'))
print(Solution().validPalindrome('aaaccbbbccaaa'))
print(Solution().validPalindrome('aaaccbbbcccaaa'))
