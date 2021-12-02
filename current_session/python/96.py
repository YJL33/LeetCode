import math
class Solution:
    def numTrees(self, n: int) -> int:
        # Catalan Number  (2n)!/((n+1)!*n!)
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))
