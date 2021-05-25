"""
909
"""
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # simply simulate
        # create a dict: key=square number, value = (i, j)
        H, W = len(board), len(board[0])
        start, goal = 1, H*W
        i, j, nxt = H-1, 0, 1
        nDict = {}
        while start <= goal:
            nDict[start] = i, j
            if j+nxt < 0 or j+nxt == W:
                i, nxt = i-1, nxt*(-1)
            else:
                j = j+nxt
            start += 1

        cnt, pos = 0, [1]
        sDict = {}          # key=square number, value=steps
        while goal not in sDict and cnt < H*W:
            cnt += 1
            tmp = []

            while pos:
                p = pos.pop()                   # empty all positions ...
                for n in [1,2,3,4,5,6]:
                    if p+n in nDict:            # valid throw
                        i, j = nDict[p+n]
                        newPos = p+n if board[i][j] == -1 else board[i][j]
                        if newPos not in sDict: # never been here before
                            sDict[newPos] = cnt
                            # print 'newPos:', newPos, 'sDict[newPos]', sDict[newPos]
                            tmp += newPos,
            pos = tmp                           # ... and replace with new positions

        # print sDict
        return sDict[goal] if goal in sDict else -1



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