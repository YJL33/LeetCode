"""
277
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        x = 0                   # celebrity
        for i in range(1,n):
            if knows(x, i):
                x = i           # celeb should know nobody, use i
        
        # now everyone AFTER x is non-celeb
        # everyone before x at least know someone
        for i in range(x):      # check if x know anyone before him
            if knows(x, i):
                return -1
        
        # verify celebrity
        for i in range(n):
            if i!= x and not knows(i, x):
                return -1
        
        return x
        

