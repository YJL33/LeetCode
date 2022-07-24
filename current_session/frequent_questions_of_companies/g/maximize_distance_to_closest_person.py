from typing import List

# simply go through whole array
# and keep update maxDist
# handle edge cases (head and tail 0s)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        while seats[i] != 1:
            i += 1
        maxDist = i                                     # from left
        
        prev = i
        for i in range(i+1, len(seats)):
            s = seats[i]
            if s == 1:
                maxDist = max(maxDist, (i-prev)/2)      # in the middle
                prev = i
        
        maxDist = max(maxDist, i-prev)                  # from right
        return int(maxDist)

print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([0,0,0,0,1]))
print(Solution().maxDistToClosest([1,0,0,0,0,1]))
