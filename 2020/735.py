'''
735
'''
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, i = [], 0
        while i < len(asteroids):
            a = asteroids[i]        # incoming asteroid
            if a > 0:
                stack.append(a)
            else:                   # incoming is negative
                while stack and 0 < stack[-1] < abs(a):
                    stack.pop()
                if stack and 0 < stack[-1] == abs(a):   # both explode
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:  # none positive left, add this negative
                    stack.append(a)
            i += 1
        return stack

# print(Solution().asteroidCollision())
print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([-2,-1,1,2]))