from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use binary search
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        row = bisect.bisect_left([r[0] for r in matrix], target)
        if row < len(matrix) and matrix[row][0] == target: return True
        row -= 1
        col = bisect.bisect_left(matrix[row], target)
        return col < len(matrix[0]) and matrix[row][col] == target
