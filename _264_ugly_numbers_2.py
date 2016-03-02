"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note that 1 is typically treated as an ugly number.
"""
import sys

class Solution(object):
    """
    Solution for LEET
    """
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]  # Ugly Numbers, must be generated from its previous element.
        twos = 0      # The order of previous element that used to generate next Ugly number (X 2)
        threes = 0    # The order of previous element that used to generate next Ugly number (X 3)
        fives = 0     # The order of previous element that used to generate next Ugly number (X 5)
        while len(uglies) < n:
            next = min(uglies[twos] * 2, uglies[threes] * 3, uglies[fives] * 5)
            if next == uglies[twos] * 2:
                twos += 1
            if next == uglies[threes] * 3:
                threes += 1
            if next == uglies[fives] * 5:
                fives += 1
            uglies.append(next)
        return uglies[-1]

sol = Solution()
sol.nth = Solution.nthUglyNumber(sol, int(sys.argv[1]))
print sol.nth
