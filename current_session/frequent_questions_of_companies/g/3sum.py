from typing import List
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        # leverage 2 sum and negative Ones
        # sort the array first
        # handle duplicate: only use the one showed up first (most left)
        if len(A) < 3: return []
        self.A = A
        self.A.sort()
        i = 0
        res = []
        while i < len(self.A) and self.A[i] <= 0:
            k = -1*self.A[i]
            pairs = self._twoSum(k, i+1)
            for p in pairs:
                res.append([self.A[i], p[0], p[1]])
            
            # increment i to next unique one
            j = i+1
            while j < len(self.A) and self.A[j] == self.A[i]: j += 1
            i = j
        return res
    
    def _twoSum(self, k, start):
        # use set/map to store seen elements
        # better use set to avoid duplicates
        res = set()
        cDict = {}
        for i in range(start, len(self.A)):
            if k-self.A[i] in cDict:
                res.add((k-self.A[i], self.A[i]))
            else:
                cDict[self.A[i]] = i
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([-2,-2,-1,0,1,2,-1,-4,4]))
print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([]))