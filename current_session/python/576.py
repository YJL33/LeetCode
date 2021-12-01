import collections
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        exitCnt = collections.defaultdict(int)
        # record the exit moves
        for i in range(m):
            for j in range(n):
                if i == 0:
                    exitCnt[(i,j)] += 1
                if i == m-1:
                    exitCnt[(i,j)] += 1
                if j == 0:
                    exitCnt[(i,j)] += 1
                if j == n-1:
                    exitCnt[(i,j)] += 1
        
        # record the neighbors
        nbDict = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                for a, b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=a<m and 0<=b<n:
                        nbDict[(i,j)].append((a,b))
                    

        moves = 0
        count = 0
        locationDict = collections.defaultdict(int)
        locationDict[(startRow, startColumn)] = 1
        while moves < maxMove:
            # count the exit moves and also add to stack
            tmp = collections.defaultdict(int)
            for k, v in locationDict.items():
                i, j = k[0], k[1]
                if (i, j) in exitCnt and moves+1 <= maxMove:
                    count += (exitCnt[(i,j)]*v)

                for a, b in nbDict[(i,j)]:
                    tmp[(a,b)] += v
                    
            moves, locationDict = moves+1, tmp
            # print('dict:', locationDict, '  cnt:', count)
        
        return count%(1000000007)

print(Solution().findPaths(2,2,2,0,0))
print(Solution().findPaths(1,3,3,0,1))
# print(Solution().findPaths(2,3,3,1,0), 'should be ?')
print(Solution().findPaths(2,3,8,1,0), 'should be 1104')
print(Solution().findPaths(7,6,13,0,2), 'should be 1659429')
print(Solution().findPaths(8,50,23,5,26), 'should be 914783380')
