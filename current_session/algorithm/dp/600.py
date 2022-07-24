from functools import lru_cache
class Solution:
    def findIntegers_dp(self, n: int) -> int:
        # use bitwise
        @lru_cache
        def f(n):       
            if n <= 2: return n+1
            return f(n-1)+f(n-2)
        
        res, prev = 0, 0
        # check everybit from left to right
        for i in range(29,-1,-1):
            if (1<<i) & n:
                res += f(i)
                if prev:            # no need to check anymore
                    break
                prev = 1
            else:
                prev = 0
        is_valid = 1 if '11' not in bin(n) else 0
        return res+is_valid

    def findIntegers(self, num: int) -> int:
        # reversed way of doing it
        # check every bit from right to left
        # calculate fibonacci while reversing
        x, y = 1, 2
        res = 0
        num += 1
        while num:
            if num & 1 and num & 2:
                res = 0
            res += x * (num&1)
            num >>= 1
            x, y = y, x+y
        return res
        

# print(Solution().findIntegers_dp(0))
# print(Solution().findIntegers_dp(1))
# print(Solution().findIntegers_dp(2))
# print(Solution().findIntegers_dp(4))
print(Solution().findIntegers_dp(10))
# print(Solution().findIntegers_dp(50))