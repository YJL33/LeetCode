import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge case
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        # binary search the correct row
        r = bisect.bisect_left([r[0] for r in matrix], target)
        if r < len(matrix) and matrix[r][0] == target: return True
        r -= 1
        c = bisect.bisect_left(matrix[r], target)
        return c<len(matrix[r]) and matrix[r][c] == target

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0))
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))