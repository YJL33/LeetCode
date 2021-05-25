"""
https://leetcode.com/problems/minimum-knight-moves/
"""
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # bfs, since the steps are mono-increasing, we can skip the points that's already visited
        # we could simplify the question by using absolute value -> but need to handle (1,1) and (0,2)
        visited = {}
        self.bfsHelper(x,y,visited)
        return visited[(0,0)]

    def bfsHelper(self,x,y,visited):
        steps = 0
        stack = [(x,y)]
        while stack:
            nodes = []
            for a,b in stack:
                a, b = abs(a), abs(b)           # optimization
                if (a,b) not in visited:
                    visited[(a,b)] = steps
                    if a == 0 and b == 0:
                        return
                    # add next layer
                    # moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]     (TLE)
                    moves = [(-1,-2),(-2,-1)]

                    if a+b == 2:                # optimization
                        moves += (-2,1),
                        moves += (-1,2),
                    for da, db in moves:
                        nodes += (a+da, b+db),
            # handle next layer
            stack = nodes
            steps += 1



                

print(Solution().minKnightMoves(1,1), Solution().minKnightMoves2(1,1), Solution().minKnightMoves(1,1) == Solution().minKnightMoves2(1,1))
print(Solution().minKnightMoves(1,0), Solution().minKnightMoves2(1,0), Solution().minKnightMoves(1,0) == Solution().minKnightMoves2(1,0))
print(Solution().minKnightMoves(2,4), Solution().minKnightMoves2(2,4), Solution().minKnightMoves(2,4) == Solution().minKnightMoves2(2,4))
print(Solution().minKnightMoves(5,5), Solution().minKnightMoves2(5,5), Solution().minKnightMoves(5,5) == Solution().minKnightMoves2(5,5))
print(Solution().minKnightMoves(-5,-5), Solution().minKnightMoves2(-5,-5), Solution().minKnightMoves(-5,-5) == Solution().minKnightMoves2(-5,-5))
print(Solution().minKnightMoves(-5,5), Solution().minKnightMoves2(-5,5), Solution().minKnightMoves(-5,5) == Solution().minKnightMoves2(-5,5))
print(Solution().minKnightMoves(5,-5), Solution().minKnightMoves2(5,-5), Solution().minKnightMoves(5,-5) == Solution().minKnightMoves2(5,-5))
print(Solution().minKnightMoves(2,20), Solution().minKnightMoves2(2,20), Solution().minKnightMoves(2,20) == Solution().minKnightMoves2(2,20))