from typing import List
import collections
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # BFS(?)
        dq = collections.deque()
        dq.append((start, 0))
        seen = set()
        while dq:
            val, steps = dq.popleft()
            if val in seen: continue
            if val == goal: return steps
            if val < 0 or val > 1000: continue
            seen.add(val)
            for n in nums:
                dq.append((val+n, steps+1))
                dq.append((val-n, steps+1))
                dq.append((val^n, steps+1))
        return -1