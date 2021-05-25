"""
118
"""
class Solution:
    def generate(self, N: int) -> List[List[int]]:
        if N == 1: return [[1]]
        if N == 2: return [[1],[1,1]]
        ans = [[1],[1,1]]

        def generateNewRow(row):
            tmp = [1]
            for i in range(1,len(row)):
                tmp.append(row[i]+row[i-1])
            return tmp
        for i in range(2, N):
            ans.append(generateNewRow(ans[-1]))
        return ans
