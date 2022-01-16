from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # O(nlogn)
        # see https://is.gd/mG0SyA
        batteries.sort()
        sumt = sum(batteries)
        while batteries[-1] > sumt//n:
            n -= 1
            sumt -= batteries.pop()
        return sumt//n
        
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Binary Search 
        # The idea is to check if we can run computers for m hours (n * m total hours). 
        # For that, we accumulate power from all batteries, 
        # taking no more than m from each. 
        # If we have enough power for n * m hours - we can run all our computers for m hours.

        # using variance of binary search template 2
        l, r = -1, sum(batteries)
        def is_valid(x):
            return sum([min(x, b) for b in batteries]) >= n*x
        while l < r:
            m = (l+r+1)//2                  # add 1 here due to r=m-1
            if is_valid(m):                 # good m, keep seek for smaller
                l = m
            else:
                r = m-1
        return int(l)
    