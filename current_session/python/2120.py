from typing import List
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # simply simulate the process

        res = []
        for i in range(len(s)):
            # go through the all ins
            cnt = 0
            currentlyAt, end = i, len(s)
            dy, dx = startPos[0], startPos[1]
            while currentlyAt != end:
                ins = s[currentlyAt]
                if ins == 'U':
                    dy -= 1
                elif ins == 'D':
                    dy += 1
                elif ins == 'R':
                    dx += 1
                elif ins == 'L':
                    dx -= 1
                if 0 <= dy < n and 0 <= dx < n:
                    cnt += 1
                    currentlyAt += 1
                else:
                    currentlyAt = end
            
            res.append(cnt)
        
        return res