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
        # Sieve of Eratosthenes Algorithm: (non-optimized)
        # Time: O(~n!)
        # Space: O(n)
        flag = [False]*(n)
        count = 0
        for i in xrange(2,n):
            if not flag[i]:         # a prime
                #print "is it prime?", i, flag[i],
                flag[i], tmp = 1, 1
                count += 1
                while tmp*i < n:
                    #print "calculating tmp.... ", tmp*i
                    flag[tmp*i] = -1
                    tmp += 1
        return count