from typing import List
class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        # rotate clock-wise 90 degree
        # mirror flip along diagonal (\)
        # mirror flip L to R (|)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i < j:
                    M[i][j], M[j][i] = M[j][i], M[i][j]
        
        # print(M)
        for i in range(len(M)):
            l, r = 0, len(M[i])-1
            while l < r:
                M[i][l], M[i][r] = M[i][r], M[i][l]
                l, r = l+1, r-1
        
        # print(M)
        return

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
