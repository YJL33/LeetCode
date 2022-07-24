from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # res.append(matrix.pop(0))
            res += matrix.pop(0)
            if matrix and matrix[0]:
                lastCol = []
                for r in matrix:
                    lastCol.append(r[-1])
                res += lastCol
                for r in matrix:
                    r.pop()
            if matrix and matrix[0]:
                lastRow = matrix.pop()
                res += lastRow[::-1]
            if matrix and matrix[0]:
                firstCol = []
                for r in matrix:
                    firstCol.append(r[0])
                res += firstCol[::-1]
                for r in matrix:
                    r.pop(0)
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[7],[9],[6]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))