import bisect
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # clarification
        # any restrictions on time/space? (e.g. timeout/memory?)
        # upper/lowerbound of matrix[i][j]?

        # use binary search
        # binary search for all row[0] and row[-1]
        # binary search for each row

        # test cast
        # case: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 11

        first = [row[0] for row in matrix]
        last = [row[-1] for row in matrix]

        i = bisect.bisect_right(first, target)-1
        j = bisect.bisect_left(last, target)

        for r in range(i,min(len(matrix), j+1)):
            x = bisect.bisect_left(matrix[r], target)
            if x < len(matrix[r]) and matrix[r][x] == target:
                return True

        return False

print(Solution().searchMatrix([[1],[3],[5]],3))
# print(Solution().searchMatrix([[1]],2))
# print(Solution().searchMatrix([[1]],1))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 1))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 2))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 4))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 5))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))