"""
241
"""
from typing import List
# import itertools
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c in '+-*':
                # print('expression: ', expression)
                # print('c', c, '@ i=', i)
                l, r = self.diffWaysToCompute(expression[:i]), self.diffWaysToCompute(expression[i+1:])
                for x in l:
                    for y in r:        
                        if c == '+':
                            res += x+y,
                        elif c == '-':
                            res += x-y,
                        else:
                            res += x*y,
        if len(res) == 0:
            res.append(int(expression))
        return res

print(Solution().diffWaysToCompute("2*3-4*5"))