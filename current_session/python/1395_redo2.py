from typing import List
import heapq
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # simply count the numbers that bigger/smaller than x from both side
        # e.g. [1,3,5,7,9] -> 6 => index = 3

        biggerL, smallerL = [0]*len(rating), [0]*len(rating)
        biggerR, smallerR = [0]*len(rating), [0]*len(rating)

        minHpL, maxHpL, minHpR, maxHpR = [rating[0]], [], [rating[~0]], []
        for i in range(1,len(rating)):
            r = rating[i]
            # make sure that minHp[0] > r > maxHp[0]
            while minHpL and minHpL[0] < r:
                x = heapq.heappop(minHpL)
                heapq.heappush(maxHpL, -1*x)
            while maxHpL and -1*maxHpL[0] > r:
                x = heapq.heappop(maxHpL)
                heapq.heappush(minHpL, -1*x)
            biggerL[i], smallerL[i] = len(minHpL), len(maxHpL)
            heapq.heappush(minHpL, r)

            # do the same at the oppposite side
            r2 = rating[~i]
            while minHpR and minHpR[0] < r2:
                x = heapq.heappop(minHpR)
                heapq.heappush(maxHpR, -1*x)
            while maxHpR and -1*maxHpR[0] > r2:
                x = heapq.heappop(maxHpR)
                heapq.heappush(minHpR, -1*x)
            biggerR[~i], smallerR[~i] = len(minHpR), len(maxHpR)
            heapq.heappush(minHpR, r2)
        
        # print(biggerL, smallerL)
        # print(biggerR, smallerR)
        cnt = 0
        for i in range(1,len(rating)):
            cnt += (biggerL[i]*smallerR[i]) + (biggerR[i]*smallerL[i])
        return cnt

print(Solution().numTeams([2,5,3,4,1]))