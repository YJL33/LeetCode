"""
1025
"""
import math
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%2)==0

print(Solution().divisorGame(4))
print(Solution().divisorGame(5))
print(Solution().divisorGame(6))
print(Solution().divisorGame(7))
print(Solution().divisorGame(8))