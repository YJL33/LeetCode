"""
286
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        stack = []
        # fill the stack with gates first
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    stack.append((i,j,0))
        
        # pop the stack until nothing left
        # check its neighbors, if not a wall => update the value
        nbs = [(1,0),(-1,0),(0,1),(0,-1)]
        while stack:
            row, col, dist = stack.pop()
            for nb in nbs:
                r2, c2 = row+nb[0], col+nb[1]
                if 0<=r2<len(rooms) and 0<=c2<len(rooms[0]) and dist+1 < rooms[r2][c2] <= INF:
                    rooms[r2][c2] = dist+1
                    stack.append((r2,c2,dist+1))
        
        # leave empty room that unable to reach a gate as is (see description)
        return
