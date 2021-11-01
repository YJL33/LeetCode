from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        for h in height:
            left.append(max(left[-1], h) if left else h)
        right = []
        for h in height[::-1]:
            right.append(max(right[-1], h) if right else h)
        right.reverse()
        water = 0

        for i in range(1,len(height)-1):
            water += min(left[i], right[i])-height[i]
        
        # print(water)
        return water
