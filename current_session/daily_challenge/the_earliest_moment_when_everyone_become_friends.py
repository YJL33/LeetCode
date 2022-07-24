from typing import List
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort and then use set operation and 'who array'
        # use an arr to store representatives (who)
        # for each a and b
        # find representative               O(logN)
        # update who and merge two sets     O(1)
        
        
        who = [i for i in range(n)]
        fd = {}                         # key: who, val: people in the group
        for i in range(n):
            fd[i] = set([i])
        
        logs.sort()
        
        for t, a, b in logs:
            # get representative and then merge their group
            while who[a] != a:
                a = who[a]
            while who[b] != b:
                b = who[b]
            
            if a != b:
                a, b = min(a,b), max(a,b)
                who[b] = a
                fd[a].union(fd[b])
                del fd[b]
            
            if len(fd) == 1:
                return t
        
        return -1