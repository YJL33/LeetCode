from typing import List
from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # simply simulate the whole process: (play all incoming requests in order)
        # we also need to:
        # 1. maintain the server status (of k servers): occupy/free the server when needed
        # 2. assign the server_id based on its availability
        # 3. count the request
        
        free_servers = SortedList([i for i in range(k)])               # all available
        request_cnt = [0 for _ in range(k)]
        busy = []
        
        for i, arrival_time in enumerate(arrival):
            # update the available servers
            while len(busy) > 0 and busy[0][0] <= arrival_time:
                _, free_id = heapq.heappop(busy)
                free_servers.add(free_id)

            # see if we have any server available
            if len(free_servers) == 0: continue

            # assign one, count+1, and free the host until then (end handling)
            server_id = free_servers[free_servers.bisect_left(i%k)%len(free_servers)]
            free_servers.remove(server_id)
            
            request_cnt[server_id] += 1
            heapq.heappush(busy, (arrival_time+load[i], server_id))
        
        res = []
        max_request_seen = max(request_cnt)
        for i in range(len(request_cnt)):
            if request_cnt[i] == max_request_seen:
                res.append(i)
        return res
                
            
            