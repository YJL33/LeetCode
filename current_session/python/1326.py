from typing import List
class Solution:
    def minTaps(self, n: int, A: List[int]) -> int:
        # use DP
        # track the uncovered location
        # for each uncovered i
        # find the farthest j that can get location i covered
        # and go to the next uncovered location (j+A[j], not j+A[j]+1, see note)
        # see if it can get covered
        # if unable to cover this location, return -1

        # note that the range between A[j] and A[j]+1 need to be covered as well

        i = 0                   # first uncovered location
        tapCnt = 0
        while i < len(A)-1:
            # print('checking i', i, A[i:])
            uncovered = i
            # check all j to see if the checking location is covered
            # if any, update the next uncovered location
            for j in range(i, n+1):
                if A[j] != 0 and j-A[j] <= uncovered:
                    i = max(i, j+A[j])
            if i == uncovered: return -1
            tapCnt += 1
        
        return tapCnt

print(Solution().minTaps(35,[1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]))