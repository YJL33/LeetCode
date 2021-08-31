from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        r2 = bisect.bisect_left([r[0] for r in matrix], target)     # from first row to r2 will include target
        if r2 < len(matrix) and matrix[r2][0] == target: return True
        r2 -= 1
        r1 = bisect.bisect_left([r[-1] for r in matrix], target)    # from r1 to the r2
        # print('r1, r2', r1, r2)
        for r in range(r1, r2+1):
            c = bisect.bisect_left(matrix[r], target)
            if matrix[r][c] == target: return True
        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 0))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 50))
        