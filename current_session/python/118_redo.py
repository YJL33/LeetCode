from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1: return res
        while len(res) < numRows:
            x = res[-1]+[0]
            y = [0]+res[-1]
            # print('x,y:',x,y)
            res.append([x[i]+y[i] for i in range(len(res)+1)])
        return res

print(Solution().generate(1))
print(Solution().generate(5))