import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # bisect
        fCol = [a[0] for a in matrix]
        if target >= fCol[-1]:      # in the last row if exist
            i = bisect.bisect_left(matrix[-1], target)
            return i<len(matrix[-1]) and matrix[-1][i] == target
        
        row = bisect.bisect_left(fCol, target)
        if row == 0:
            return matrix[0][0] == target

        if matrix[row][0] == target:
            return True
        else:
            pos = bisect.bisect_left(matrix[row-1], target)
            return pos<len(matrix[row]) and matrix[row-1][pos] == target

print(Solution().searchMatrix([[1],[3],[5]],3))
# print(Solution().searchMatrix([[1]],2))
# print(Solution().searchMatrix([[1]],1))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 1))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 2))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 4))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 5))
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))