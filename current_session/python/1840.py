from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        # get all spans, and fill each span    
        # however, there can be lots of restrictions on both sides,
        # and sometimes the adjacent restrictions are not the tightest bound.
        # We solve this issue by "propagating" restrictions from left to right and then from right to left.
        # (tighten all restrictions)

        if not restrictions: return n-1
        restrictions.append([1,0])
        restrictions.append([n,n-1])
        restrictions.sort()

        L = len(restrictions)

        for i in range(1,L):
            dw = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1]+dw)
        
        for j in range(L-2, -1, -1):
            dw = restrictions[j+1][0] - restrictions[j][0]
            restrictions[j][1] = min(restrictions[j][1], restrictions[j+1][1]+dw)
        
        ans = 0
        for i in range(1,L):
            l, h1 = restrictions[i-1]
            r, h2 = restrictions[i]
            ans = max(ans, max(h1,h2)+(r-l-abs(h1-h2))//2 )
        
        return ans


        

print(Solution().maxBuilding(100,[[68,29],[89,27],[66,26],[34,9],[53,23],[93,24],[70,12],[25,24],[5,4],[94,41],[51,42],[6,39],[55,21],[69,9],[39,50],[99,42],[77,24],[81,46],[90,43],[27,14],[31,5],[67,37],[82,10],[26,47],[84,34],[37,30],[83,39],[21,39],[49,39],[13,48],[12,34],[57,0],[7,43],[17,6],[23,0],[86,30],[47,30],[61,19],[30,49],[95,42],[3,31],[33,36],[11,45],[75,39],[85,46],[29,33],[2,9],[22,17],[65,42],[96,0],[35,46],[88,47],[74,0],[73,47],[41,45],[15,21],[97,0],[64,0],[40,21],[76,2],[54,3],[24,33],[45,24],[16,23],[91,14],[43,35],[79,6],[46,30],[71,3],[9,39],[50,21],[48,45],[63,42],[58,3],[10,26],[4,6],[52,19],[32,39],[87,50],[8,48],[19,25],[92,1],[28,21],[59,31],[72,24],[78,9],[100,8],[60,20],[42,16],[38,8],[62,31],[36,22],[44,27],[14,45],[18,3],[98,0],[20,1],[56,24],[80,3]]), '== 13')