from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        visited.add(start)
        dq = deque()
        dq.append(start)
        while dq:
            x = dq.popleft()
            visited.add(x)
            if arr[x] == 0:
                return True
            if x+arr[x] < len(arr) and x+arr[x] not in visited:
                dq.append(x+arr[x])
            if x-arr[x] >= 0 and x-arr[x] not in visited:
                dq.append(x-arr[x])
        
        return False
    