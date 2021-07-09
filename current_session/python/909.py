"""
909
"""
class Solution(object):
    def __init__(self):
        self.minSeen = float('inf')

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # simply simulate
        # create a dict: key=square number, value = (i, j)
        H, W = len(board), len(board[0])
        goal = H*W
        self.minSeen = H*W
        sqn, i, j, nxt = 1, H-1, 0, 1
        sDict = {}
        
        while sqn <= goal:
            sDict[sqn] = (i,j)
            if (j+nxt) < 0 or (j+nxt) >= W:      # change row
                i -= 1
                nxt = nxt*-1
            else:
                j = j+nxt
            sqn += 1
        
        seenCntDict = {}

        # dfs
        def dfs(cnt, start):
            # too many steps
            if cnt>self.minSeen:
                return
            if start in seenCntDict and cnt >= seenCntDict[start]:
                return
            if start == goal:
                self.minSeen = min(self.minSeen, cnt)
                return
            
            nextSqn = []
            for x in [1,2,3,4,5,6]:
                if start+x in sDict:
                    i, j = sDict[start+x]
                    if board[i][j] != -1:
                        nextSqn += board[i][j],
                    else:
                        nextSqn += start+x,

            seenCntDict[start] = cnt
            for n in nextSqn:
                dfs(cnt+1, n)
                
        dfs(0, 1)
        return self.minSeen if self.minSeen != H*W else -1
    



print(Solution().snakesAndLadders([
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]))

print(Solution().snakesAndLadders([
[1,1,1,1,1,-1],
[-1,-1,-1,-1,-1,1],
[-1,-1,-1,-1,-1,-1],
[-1,34,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]))