from typing import List
import collections
class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        # naive approach:
        # calculate mean of each span
        # O(n^2)
        # then use dfs to find all possible combinations

        meanMap = collections.defaultdict(float)
        for i in range(len(A)):
            localSum = A[i]
            for j in range(i+1,len(A)+1):
                meanMap[(i,j)] = localSum / (j-i)
                if j<len(A): localSum += A[j]
        # print(meanMap)

        # dfs
        solMap = collections.defaultdict(float)

        def dfs(start, newK):
            if start>=len(A) or newK == 0: return float('-inf')
            if (start, newK) in solMap: return solMap[(start, newK)]
            if newK == 1: return meanMap[(start, len(A))]
            if newK == len(A[start:]): return sum(A[start:])
            sol = 0
            for j in range(start+1, len(A)+1):
                sol = max(sol, meanMap[(start,j)] + dfs(j, newK-1))
            solMap[(start, newK)] = sol
            return sol
        
        return dfs(0,k)

print(Solution().largestSumOfAverages([9,1,2,3,9], k = 3))
print(Solution().largestSumOfAverages([1,2,3,4,5,6,7], k = 4))