from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # simply simulate the process

        start, cur, end = 0, 0, len(gas)-1
        tank = gas[0]-cost[0]
        while cur != end:
            if tank < 0:
                start, end = start-1, end-1
                if start < 0: start += len(gas)
                tank += gas[start]-cost[start]
            else:
                cur += 1
                tank += gas[cur]-cost[cur]
        
        return start if (tank >= 0) else -1
