"""
332
"""
from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create ticket dict
        # sort by lexical order
        self.td = collections.defaultdict(list)
        tickets.sort()
        for i in range(len(tickets)):
            s, e = tickets[i]
            self.td[s].append((e, i))    # destination is naturally sorted by lexical order

        # use DFS + used ticket
        self.usedTkt = set()
        self.res = []
        def dfs(x):
            if len(self.usedTkt) == len(tickets): return True
            for destination, tkt in self.td[x]:
                if tkt not in self.usedTkt:
                    self.res.append(tkt)
                    self.usedTkt.add(tkt)
                    tmp = dfs(destination)
                    # restore
                    if not tmp:
                        self.usedTkt.remove(tkt)
                        self.res.pop()
                    else:
                        return True
            return False
        
        dfs('JFK')
        return [tickets[self.res[0]][0]] + [tickets[x][1] for x in self.res]

print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))