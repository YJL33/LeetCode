from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        num_set = set([i for i in range(1, N+1)])
        for i in range(N):
            if set(matrix[i]) != num_set:
                return False
            if set([row[i] for row in matrix]) != num_set:
                return False
        return True