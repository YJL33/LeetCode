"""
332
"""
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # dfs?
        # dict: key=start, value=(end, ith ticket)
        # start from JFK
        # from its endpoints, start by the lexical order
        # if all of the tickets are used: return nothing

        td = collections.defaultdict(list)
        tickets.sort()
        for i in range(len(tickets)):
            t = tickets[i]
            td[t[0]].append((t[1], i))

        def dfs(s, used=set()):
            # search by lexical order
            # print s, used
            if len(used) == len(tickets):
                return [True]
            res = []
            for t in td[s]:
                end, tktOrd = t
                if tktOrd not in used:
                    res += tktOrd,
                    used.add(tktOrd)
                    tmp = dfs(end,used)
                    if not tmp:
                        used.remove(tktOrd)
                        res.pop()
                    else:
                        return res+tmp

        ans = dfs('JFK')
        # print ans
        return [tickets[ans[0]][0]]+[tickets[i][1] for i in ans[:-1]]

print Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])