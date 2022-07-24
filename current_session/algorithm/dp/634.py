from functools import lru_cache
import sys
class Solution:
    def findDerangement(self, n: int) -> int:
        # e.g. n=4
        # say we have dp(3), append 4 at the end of all derangements ans swap 4 with all of them
        # (n-1)*dp(3)
        # we also can generate by (n-1)*dp(2), where represents "derangements-to-be" (has one element at its original position), and then swap it with 4

        # sys.setrecursionlimit(100000)
        # print('limit', sys.getrecursionlimit())
        # @lru_cache
        # def dp(n):
        #     if n == 1: return 0
        #     if n == 2: return 1
        #     if n == 3: return 2
        #     return (n-1)*(dp(n-1)+dp(n-2))%1000000007
        # return dp(n)

        # use bottom-up DP
        if n <= 3: return n-1
        a, b = 1, 2
        x = 3
        while x < n:
            a, b = b, x*(a+b)%1000000007
            x += 1
        return b

print(Solution().findDerangement(100))
print(Solution().findDerangement(1000))
print(Solution().findDerangement(10000))