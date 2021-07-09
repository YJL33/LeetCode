"""
343
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        if n == 3:
            return 2
        if n > 3:
            if n % 3 == 2:
                return 2*(3**(n//3))
            if n % 3 == 1:
                return 2*2*(3**((n//3)-1))
            if n % 3 == 0:
                return 3**(n//3)