"""
767
"""
import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # we want a counter
        size = len(S)
        cd = collections.defaultdict(int)
        limit = size//2
        maxCnt, mostFreq = 0, ""
        for c in S:
            cd[c] += 1
            if cd[c] > limit:
                return ""
            if cd[c] > maxCnt:
                maxCnt, mostFreq = cd[c], c

        return self.org(cd)

    def org(self, cd):
        for k in cd.keys():
