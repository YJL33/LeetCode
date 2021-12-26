"""
878. Nth Magical Number
Hard

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.
"""
import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # given the repeating pattern, the magical numbers will be nothing but the pattern + gcd*x
        # e.g. say we have a, b = 6, 10
        # pattern = [6,12,18,10,20,24,30]
        # sort the pattern and simply calculate the result
        gcd = math.gcd(a, b)
        lcm = (a*b)//gcd
        cand = [a*i for i in range(1, lcm//a)] + [b*i for i in range(1, lcm//b)] + [lcm]
        cand.sort()
        return (cand[(n-1)%len(cand)] + lcm*((n-1)//len(cand))) % 1000000007
        
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # binary search within the range
        # see how many magical numbers are ahead of given number x
        # 
        l, r = min(a,b), n*min(a,b)
        lcm = (a*b)//math.gcd(a,b)
        while l < r:
            m = (l+r)//2
            if m//a + m//b - m//lcm < n:        # too few
                l = m+1
            else:                               # more or equal to n
                r = m
        return r%1000000007

    def nthMagicalNumber_TLE(self, n: int, a: int, b: int) -> int:
        # simply increase a and b
        x, y = 1, 1
        if n == 1:
            return min(a, b)%1000000007
        if a == b or b%a == 0:
            return a*n%1000000007

        # make sure a <= b
        if a > b:
            return self.nthMagicalNumber(n, b, a)

        cnt = 1
        while cnt < n:
            if x*a < y*b:
                x += 1
            else:
                y += 1
            if x*a == y*b:
                x += 1
            cnt += 1
        
        return min(x*a, y*b)%1000000007

print(Solution().nthMagicalNumber(1000000000,40000,40000))
print(Solution().nthMagicalNumber(1000000000,39999,40000))
