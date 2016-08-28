"""
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratosthenes Algorithm: (optimized)
        # Time: O(n log log n)
        # Space: O(n)

        # 1. scanning begin i, end with n
        # 2. any number n will have a factor <= sqrt(n)
        #    therefore, just need to check primes that <= sqrt(n)
        if n < 3:
            return 0
        #np1 = n + 1
        s = [True] * n
        s[0] = s[1] = False
        sqrtn = int(round(n**0.5))
        for i in xrange(2, sqrtn + 1):                              # opt.2
            if s[i]:
                s[i*i: n: i] =  [False] * len(xrange(i*i, n, i))    # opt.1
        return s.count(True)