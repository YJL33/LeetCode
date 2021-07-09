'''
125
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        return s == s[::-1]