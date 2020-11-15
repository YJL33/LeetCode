"""
https://leetcode.com/problems/analyze-user-website-visit-pattern/
"""
import collections
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
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

        meta = []
        for i in range(len(username)):
            meta.append((timestamp[i], username[i], website[i]))

        meta = sorted(meta, key=lambda item:item[0])
        # 0, 1, 2 = ts, user, site
        # print(meta)

        resDct = collections.defaultdict(list)
        usr = collections.defaultdict(list)
        maxSeen = 0

        for i in range(len(meta)):
            usr[meta[i][1]].append((meta[i][0], meta[i][2]))

            if len(usr[meta[i][1]]) >= 3:
                history = usr[meta[i][1]]
                for a in range(len(history)-2):
                    for b in range(a+1,len(history)-1):
                        if meta[i][1] not in resDct[(history[a][1],history[b][1],meta[i][2])]:
                            resDct[(history[a][1],history[b][1],meta[i][2])] += meta[i][1],
                        maxSeen = max(maxSeen, len(resDct[(history[a][1],history[b][1],meta[i][2])]))

        items, res = resDct.items(), []
        for k, v in items:
            if len(v) == maxSeen: res += k,
        tmp = sorted(res)[0]

        return [tmp[0], tmp[1], tmp[2]]

# print(Solution().mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]))
print(Solution().mostVisitedPattern(["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]))

