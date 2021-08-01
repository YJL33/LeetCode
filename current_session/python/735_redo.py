from typing import List
class Solution:
    def astCollision(self, A: List[int]) -> List[int]:
        stack = []
        for a in A:
            if a > 0:
                stack.append(a)
            else:
                while stack and 0<stack[-1]<(-1*a):
                    stack.pop()
                if stack and stack[-1]==(-1*a):
                    stack.pop()
                elif (len(stack) == 0 or stack[-1]<0):
                    stack.append(a)
        return stack