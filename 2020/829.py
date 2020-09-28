"""
see https://leetcode.com/problems/consecutive-numbers-sum/
"""
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # find x s.t. xk + k*(k+1)/2 = N
        # x = N/k - (k+1)/2
        # x must > 0
        counter = 0
        k = 1
        while k*(k+1)/2 <= N:
            if (1.0*N/k - (k+1)/2.0).is_integer():
                counter += 1
            k += 1
        return counter
        
print(Solution().consecutiveNumbersSum(15))
print(Solution().consecutiveNumbersSum(5))
print(Solution().consecutiveNumbersSum(9))