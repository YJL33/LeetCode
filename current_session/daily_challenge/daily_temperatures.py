from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # use monotonic stack
        ms = []
        res = [0 for _ in T]
        for i in range(len(T)):
            while ms and T[i] > T[ms[-1]]:
                j = ms.pop()
                res[j] = i-j
            ms.append(i)
            # print('t:', T[i], 'res:', res)
        
        return res

print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
