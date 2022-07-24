import heapq
from typing import List
class Solution:
    # clarification:
    # any restrictions on time/space? (e.g. timeout/memory?)
    # is there only one valid solution? or could be more than one?
    # upper/lowerbound of grid[i][j]/height/width
    
    # naive approach
    # try all possible routes, note that it's not shortest path, so there could be many many routes
    # tc: rough estimation O(4^N), where N is the number of grids
    
    # dp?
    # if we looking at the ending position, then dp[-1][-1] is the value of grid[-1][-1]
    # define dp(i, j) is the score starting from (i,j) to (m-1, n-1)
    # however, in each point, we can go to any direction
    # dp(i-1, j) = min(grid[i-1][j], dp(i, j))
    # need to update backward, not a good idea
    
    # bfs with heap (dijkstra)
    # starting from x, and move to any direction and put the move into heap
    # heap is popped based on min score
    # avoid moving to previous position, or use a dict to store the max min score in each position
    # tc:
    # consider heap size, worst case we store all positions in heap (size mn), and we need to operate mn times
    # should be propotional to size of grid, tc = O(mnlogmn), where N=mn
    # sc: 
    # O(mn) for seen array, O(mn) for the heap size
    
    # optimization
    # remove previ and prevj, since we've already use seen array
    # pros: save some memory, and comparison in each operation
    # cons: add more heap opeartion, which will cost additional ~33-50% O(logMN) insert/pop
    
    # see more at
    # https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/416227/Python-Dijkstra-Binary-Search-%2B-DFS-Union-Find-complexity-analysis
    
    # test case
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[-1 for _ in range(n)] for _ in range(m)]
        hp = [(-1*grid[0][0],0,0,m,n)]          # wanna use max-heap, but built-in heap is min-heap. use negative scores
        
        while hp:
            score, i, j, pi, pj = heapq.heappop(hp)
            score = -1*score            # convert it back
            if i == m-1 and j == n-1:   # termination
                return score
            if seen[i][j] >= score:     # we've been here with higher score
                continue
            seen[i][j] = score
            for a,b in [(i+1,j), (i-1,j), (i,j+1),(i,j-1)]:             # make moves
                if 0<=a<m and 0<=b<n and (a!=pi or b!=pj):
                    heapq.heappush(hp, (-1*min(score, grid[a][b]), a,b,i,j))    # convert to negative when push into heap
            # print('hp', hp)
        return -1           # should not reach this line
            
        