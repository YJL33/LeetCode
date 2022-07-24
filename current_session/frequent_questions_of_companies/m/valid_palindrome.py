class Solution:
    def isPalindrome(self, s:str) -> bool:
        def next(i, isL=True):
            dx = 1 if isL else -1
            i += dx
            while 0<=i<len(s) and s[i].lower() not in '0123456789abcdefghijklmnopqrstuvwxyz':
                i += dx
            return i
                
        l, r = next(-1, True), next(len(s), False)
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l, r = next(l, True), next(r, False)
        return True