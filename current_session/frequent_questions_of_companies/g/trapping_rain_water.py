from typing import List
class Solution:
    def trap(self, H: List[int]) -> int:
        rMax = [H[-1]]
        for i in range(len(H)-1, -1, -1):
            rMax.append(max(H[i], rMax[-1]))
        rMax.reverse()

        lMax = H[0]
        ans = 0
        for i in range(len(H)-1):
            wall = min(lMax, rMax[i])
            if H[i] < wall:
                ans += wall-H[i]
            lMax = max(H[i], lMax)
        
        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,0,3,2,5]))