"""
see https://leetcode.com/problems/spiral-matrix/
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        moves = 0
        while matrix:
            if moves%4 == 0:
                r = matrix.pop(0)
                for a in r:
                    output += a,
            elif moves%4 == 1:
                for r in matrix:
                    output += r.pop(),
            elif moves%4 == 2:
                r = matrix.pop()
                for a in r[::-1]:
                    output += a,
            else:
                for r in matrix[::-1]:
                    output += r.pop(0),
            moves += 1
            matrix = [x for x in matrix if len(x)>0]
            # print(matrix)

        return output
        
print(Solution().spiralOrder([[7],[9],[6]]))