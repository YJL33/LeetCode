from typing import List
import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # simply use BFS
        # craft an employee map first
        # key: manager, value: subordinate
        md = collections.defaultdict(list)
        for i in range(len(manager)):
            md[manager[i]].append(i)

        dq = collections.deque()
        dq.append((headID, 0))
        timePassed = 0
        while dq:
            # print('current stack:', stack)
            x, prevT = dq.popleft()
            timePassed = max(timePassed, prevT+informTime[x])
            for e in md[x]:
                dq.append((e, prevT+informTime[x]))
        
        return timePassed

print(Solution().numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
print(Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
print(Solution().numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
print(Solution().numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(Solution().numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]))
print(Solution().numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337]))
