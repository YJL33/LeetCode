'''
811
'''
import collections
from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dd = collections.defaultdict(int)
        for x in cpdomains:
            cnt, url = x.split(' ')
            dd[url] += int(cnt)
            for j in range(len(url)-1, -1, -1):
                if url[j] == '.':
                    dd[url[j+1:]] += int(cnt)
        res = []
        for i, j in dd.items():
            res.append(str(j) + ' ' + i)
        return res

print(Solution().subdomainVisits(["100 discuss.leetcode.com"]))