"""
https://leetcode.com/problems/beautiful-arrangement/
"""
import collections
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # use dict:
        # key = number (length) of elements + elements used in permutations
        # value = count
        pd = collections.defaultdict(int)
        def helper(i,X):
            if i == 1:
                return 1
            if (i,X) in pd:
                return pd[(i,X)]
            tot = 0
            for j in range(len(X)):
                if X[j]%i==0 or i%X[j]==0:
                    tot += helper(i-1, X[:j]+X[j+1:])
            pd[(i,X)] = tot
            return tot

        return helper(N, tuple(range(1,N+1)))

print Solution().countArrangement(4)
print Solution().countArrangement(15)
