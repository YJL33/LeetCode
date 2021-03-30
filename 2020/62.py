"""
62
"""
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # math
        # the combination of (n-1) "right" and (m-1) "down"
        a = math.factorial(m-1)
        b = math.factorial(n-1)
        return int(math.factorial(m+n-2)/ (a*b))