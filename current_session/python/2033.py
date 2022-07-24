from typing import List
# weekly contest 262
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        H, W = len(grid), len(grid[0])
        A = []
        for i in range(H):
            for j in range(W):
                A.append(grid[i][j])
        A.sort()
        target, ans = A[H*W//2], 0
        for a in A:
            if (abs(a-target)%x != 0): return -1
            ans += abs(a-target)//x
        return ans
