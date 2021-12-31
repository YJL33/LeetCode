from typing import List
class Solution:
    def maxDistance(self, A: List[List[int]]) -> int:
        l = [0,1] if A[0][0] < A[1][0] else [1,0]       # the smaller the better
        r = [0,1] if A[0][-1] > A[1][-1] else [1,0]     # the bigger the better
        # print('l, r', l, r)
        for i in range(2,len(A)):
            a, b = A[i][0], A[i][-1]
            l0, l1 = l
            r0, r1 = r
            if a < A[l1][0]: l = [l0, i] if A[l0][0] < a else [i, l0]
            if b > A[r1][-1]: r = [r0, i] if A[r0][-1] > b else [i, r0]
            
        # print('l, r', l, r)
        return A[r[0]][-1]-A[l[0]][0] if l[0] != r[0] else max(A[r[1]][-1]-A[l[0]][0], A[r[0]][-1]-A[l[1]][0])

print(Solution().maxDistance([[1,4],[0,5]]))
print(Solution().maxDistance([[-1,1],[-3,1,4],[-2,-1,0,2]]))
