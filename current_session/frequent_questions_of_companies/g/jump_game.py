from typing import List
class Solution:
    def canJump(self, A: List[int]) -> bool:
        # keep update how far we can reach
        reach = A[0]            # we can reach this index
        cur = 0
        while cur < len(A) and cur <= reach:
            # print('cur, reach', cur, reach)
            reach = max(reach, cur+A[cur])
            cur += 1
        return reach >= len(A)-1

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([1,1,1,1,1,1,1,1]))
print(Solution().canJump([1,4,1,1,1,1,1,0,1]))
