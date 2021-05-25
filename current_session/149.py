"""
149
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # use dictionary
        # key: line, val: points
        
        if len(points) <= 2: return len(points)

        ld = {}
        visited = set()
        ans = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                A, B = points[i], points[j]
                if (i,j) not in visited:
                    visited.add((i,j))
                    L = self.getLine(A, B)
                    if L in ld:
                        ld[L] += j,
                        for k in ld[L]:
                            visited.add((k,j))
                        ans = max(ans, len(ld[L]))
                    else:
                        ld[L] = [i, j]
                        ans = max(ans, 2)
        return ans

    def getLine(self, A, B):
        # slope(m) and intersect (-b/m)
        # y = mx + b
        x1, y1, x2, y2 = A[0], A[1], B[0], B[1]
        if x2 == x1:
            return (str(x1), float('inf'))
        m = 1.0*(y2-y1)/(x2-x1)
        b = y1-m*x1
        return (m, b)

