"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # start from top-right or left-bottom
        if not matrix: return False
        i, j = 0, len(matrix[0])-1

        while i<len(matrix) and 0<=j:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:     # not in this col
                j -= 1
            else:                           # not in this row
                i += 1
        return False

print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))