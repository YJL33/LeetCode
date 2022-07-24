from typing import List
class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        i, j, mv = -1, -1, -1
        H, W = len(A), len(A[0])
        res = []
        self.seen = set()

        def nextPos(x, y, mv):
            if (x,y,mv) == (-1,-1,-1): return 0, 0, 0
            moves = [(0,1),(1,0),(0,-1),(-1,0)]
            dx, dy = moves[mv%4]
            while (x+dx, y+dy) in self.seen or x+dx<0 or x+dx==H or y+dy<0 or y+dy==W:
                mv += 1
                dx, dy = moves[mv%4]
            x, y = x+dx, y+dy
            return x, y, mv

        while len(res) < H*W:
            i, j, mv = nextPos(i, j, mv)
            res.append(A[i][j])
            self.seen.add((i,j))
        return res

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
