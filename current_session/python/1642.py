from typing import List
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # naive approach (brute force)
        # first, we're only interested in those places that needs ladder/bricks
        # so in the end we'll stop at either the end or in front of a place above
        
        # keep tracking the usage of bricks
        # and if the sum of usage is more than bricks we have, (we'll need ladder anyway)
        # use the ladder at the 'biggest gap', and minus from the sum of usage
        
        # the other way around is to use bricks optimally:
        # keep add gaps into the heap, and we only pop out the 'smallest gap' for brick usage
        
        # time O(N*logN), where N is the length of heights
        # 'places' are propotional with N, and for each place we'll need heap push/pop
        # space O(N)
        
        prev = float('inf')
        hp = []                         # heap of brick usage
        brick_needed = 0                # sum of gaps

        for i in range(len(heights)):

            # use ladder optimally
            if heights[i] > prev:
                brick_needed += heights[i]-prev
                heapq.heappush(hp, prev-heights[i])
                if brick_needed > bricks:
                    if ladders > 0:
                        brick_needed += heapq.heappop(hp)       # max heap (update brick_needed so we don't need so much)
                        ladders -= 1
                    else:
                        return i-1

            # use bricks optimally
            # if heights[i] > prev:
            #     heapq.heappush(hp, heights[i]-prev)          
            # if len(hp) > ladders:
            #     brick_needed += heapq.heappop(hp)
            # if brick_needed > bricks:
            #     return i-1

            prev = heights[i]
            

        return len(heights)-1