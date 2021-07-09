"""
see https://leetcode.com/problems/minimum-knight-moves/
"""
class Solution(object):

    # use absolute value and dfs
    def minKnightMoves2(self, x, y):
        def dfs(x, y):
            # print('x, y',x, y)
            if (x, y) not in seen:
                x, y = abs(x), abs(y)
                if x == y == 0:
                    return 0
                if x + y == 2:
                    return 2
                ans = min(dfs(x-1,y-2),dfs(x-2,y-1))+1
                seen[(x,y)] = ans
            return seen[(x,y)]
        seen = {}

        return dfs(x, y)
        

    # naive approach
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # bfs
        # TLE!!!
        x, y = abs(x), abs(y)
        queue = [(x,y,0)]
        seen = {(x,y):0}
        while queue:
            # print(queue)
            a, b, n = queue.pop(0)
            a, b = abs(a), abs(b)
            # if a == 0 and b == 0:
            #     return n
            if a + b == 2:
                return n+2
            else:
                if (a-2, b-1) not in seen:
                    if a-2 == 0 and b-1 == 0:
                        return n+1
                    queue += (a-2, b-1, n+1),
                if (a-1, b-2) not in seen:
                    if a-1 == 0 and b-2 == 0:
                        return n+1
                    queue += (a-1, b-2, n+1),
                # print(queue)

        return seen[(x,y)]

print(Solution().minKnightMoves(1,1) == Solution().minKnightMoves2(1,1))
print(Solution().minKnightMoves(1,0) == Solution().minKnightMoves2(1,0))
print(Solution().minKnightMoves(2,4) == Solution().minKnightMoves2(2,4))
print(Solution().minKnightMoves(5,5) == Solution().minKnightMoves2(5,5))
print(Solution().minKnightMoves(-5,-5) == Solution().minKnightMoves2(-5,-5))
print(Solution().minKnightMoves(-5,5) == Solution().minKnightMoves2(-5,5))
print(Solution().minKnightMoves(5,-5) == Solution().minKnightMoves2(5,-5))
print(Solution().minKnightMoves(2,20) == Solution().minKnightMoves2(2,20))