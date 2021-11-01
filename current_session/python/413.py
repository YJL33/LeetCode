from typing import List
# use DP
# use diff of A[i+1] and A[i]
# get the maximum length of arithmetic slices of same diff -> convert to the number
# go throught the whole array

class Solution:
    def __init__(self):
        self.ldict = {}

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        diff = A[1]-A[0]
        diffL = 0
        count = 0
        for i in range(1, len(A)-1):
            if diff == A[i+1]-A[i]:
                diffL += 1
            else:            
                count += self.convertToCnt(diffL)
                diff, diffL = A[i+1]-A[i], 0
        count += self.convertToCnt(diffL)
        return count
    
    def convertToCnt(self, L):
        # print('L', L)
        if L in self.ldict: return self.ldict[L]
        x, ans = 1, 0
        while x <= L:
            ans += x
            x += 1
        self.ldict[L] = ans
        # print(self.ldict[L])
        return ans

print(Solution().numberOfArithmeticSlices([1,2,3,8,9,10]))
print(Solution().numberOfArithmeticSlices([1]))