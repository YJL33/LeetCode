from typing import List
import heapq
import collections
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # use a minHeap of time
        hp = []
        for i in range(len(meetings)):
            t = meetings[i][-1]
            heapq.heappush(hp, (t, i))
        res = set([0,firstPerson])
        currentTime = hp[0][0]
        while hp:
            # build a undirectional graph here
            adj = collections.defaultdict(list)
            startFrom = []
            while hp and hp[0][0] == currentTime:
                t, i = heapq.heappop(hp)
                a, b, _ = meetings[i]
                if a in res or b in res:
                    res.add(a)
                    res.add(b)
                    startFrom.append(a)
                    startFrom.append(b)
                else:
                    adj[a].append(b)
                    adj[b].append(a)
            
            visited = set()
            while startFrom:
                x = startFrom.pop()
                visited.add(x)
                for p in adj[x]:
                    if p not in res:
                        res.add(p)
                    if p not in visited:
                        startFrom.append(p)
                
            if hp:
                # next current time
                currentTime = hp[0][0]
        
        return list(res)
            
            
print(Solution().findAllPeople(6,[[1,2,5],[2,3,8],[1,5,10]],1))
print(Solution().findAllPeople(4,[[3,1,3],[1,2,2],[0,3,3]],3))
print(Solution().findAllPeople(5,[[3,4,2],[1,2,1],[2,3,1]],1))
print(Solution().findAllPeople(6,[[0,2,1],[1,3,1],[4,5,1]],1))