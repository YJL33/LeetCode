from typing import List
import collections
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])
        layerDict = collections.defaultdict(list)
        for i in range(M):
            for j in range(N):
                layerDict[i+j].append(mat[i][j])
        # print(layerDict)
        res = []
        for layer in range(M+N-1):
            if layer%2:
                res += layerDict[layer]
            else:
                res += layerDict[layer][::-1]
        return res
        