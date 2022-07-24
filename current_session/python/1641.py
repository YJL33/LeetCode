class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5
        dp = [1,1,1,1,1]
        for _ in range(n-1):
            a,e,i,o,u = dp
            dp = [a, e+a, a+e+i, a+e+i+o, sum(dp)]
        return sum(dp)
