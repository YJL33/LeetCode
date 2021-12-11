from typing import List
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # simply go through twice
        # L -> R
        prevL, prevR = security[0], security[-1]
        dec = [0 for _ in security]
        inc = [0 for _ in security]
        for i in range(1,len(security)):
            if prevL >= security[i]:
                dec[i] = 1+dec[i-1]
            else:
                dec[i] = 0
            if prevR >= security[~i]:
                inc[~i] = 1+inc[~(i-1)]
            else:
                inc[~i] = 0
            prevL, prevR = security[i], security[~i]
        
        # print('inc:', inc)
        # print('dec:', dec)
        res = []
        for i in range(len(security)):
            if inc[i] >= time and dec[i] >= time:
                res += i,
        
        return res

print(Solution().goodDaysToRobBank([5,3,3,3,5,6,2], time = 2))