"""
9
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0: return x==0
        else:
            arr = str(x)
            return arr == arr[::-1]