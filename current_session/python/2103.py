class Solution:
    def countPoints(self, rings: str) -> int:
        # simply use a dict
        arr = [[0,0,0] for i in range(10)]
        color = {'R':0, 'G':1, 'B':2}
        for i in range(0, len(rings), 2):
            r = rings[i:i+2]
            # print('r', r)
            index = int(r[1])
            c = color[r[0]]
            arr[index][c] = 1
        
        cnt = 0
        for a in arr:
            if all(a): cnt += 1
        
        return cnt

print(Solution().countPoints("B0B6G0R6R0R6G9"))
print(Solution().countPoints("B0R0G0R9R0B0G0"))
print(Solution().countPoints("G4"))