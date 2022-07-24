from typing import List
class Solution:
    def findMissingRanges(self, A:List[int], lower:int, upper:int) -> List[str]:
        result = []
        A.append(upper+1)
        prev = lower - 1
        for a in A:
            if (a == prev + 2):
                result.append(str(prev+1))
            elif (a > prev + 2):
                result.append(str(prev+1) + "->" + str(a-1))
            prev = a
        return result

print(Solution().findMissingRanges(A = [0,1,3,50,75], lower = -10, upper = 99))
print(Solution().findMissingRanges([],1,1))
print(Solution().findMissingRanges([],-3,-1))
print(Solution().findMissingRanges([-1],-2,-1))
print(Solution().findMissingRanges([-1],-1,60))
print(Solution().findMissingRanges([-1],-1,-1))
print(Solution().findMissingRanges(A = [0,1,3,50,75], lower = 5, upper = 55))