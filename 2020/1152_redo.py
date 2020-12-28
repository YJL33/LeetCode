"""
https://leetcode.com/problems/analyze-user-website-visit-pattern/
"""
import collections
import itertools
class Solution(object):
    def mostVisitedPattern(self, usr, ts, site):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # naive approach:

        # for each user, once they visit more than 3 sites:
        # put it into a dict and add 1
        # once they visit 4 sites:
        # put each combination into dict and add 1
        # N sites -> N^3 combinations

        meta = [(ts[i], usr[i], site[i]) for i in range(len(usr))]
        meta.sort(key=lambda x:x[0])

        combDct = collections.defaultdict(int)
        usrSiteHist = collections.defaultdict(list)
        usrComb = {}                # key: usr, value: dict: {k=comb, v=1}
        maxSeen, maxComb = 0, ('z','z','z')

        for u in usr:
            if u not in usrComb:
                usrComb[u] = {}

        for i in range(len(meta)):
            t, u, s = meta[i]
            usrSiteHist[u].append(s)

            if len(usrSiteHist[u]) >= 3:
                # generate the combination here
                combs = itertools.combinations(usrSiteHist[u],3)
                for c in combs:
                    if c not in usrComb[u]:
                        usrComb[u][c] = 1
                        combDct[c] += 1
                        maxSeen = max(maxSeen, combDct[c])

        items, res = combDct.items(), []
        for k, v in items:
            if v == maxSeen:
                res += k,

        tmp = sorted(res)[0]
        ans = [tmp[0],tmp[1],tmp[2]]
        # ans.sort()
        return ans

print(Solution().mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"],[1,2,3,4,5,6,7,8,9,10],["home","about","career","home","cart","maps","home","home","about","career"]))
