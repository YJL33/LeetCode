"""
see https://leetcode.com/problems/group-anagrams/
"""
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # convert the strs to char cnt
        tbl = [[0 for _ in range(26)] for _ in strs]
        for i in range(len(strs)):
            for c in strs[i]:
                tbl[i][ord(c)-ord('a')] += 1

        td = collections.defaultdict(list)     # key: tbl, value: list of indexes
        for i in range(len(tbl)):
            t = ''.join(map(bin, tbl[i]))
            td[t].append(i)

        res = []
        items = td.items()
        for item in items:
            res += [strs[i] for i in item[1]],

        return res

    # trick using tuple(sorted(s))
    def groupAnagrams_2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # cnt = collections.Counter([tuple(sorted(s)) for s in strs])
        cd = collections.defaultdict(list)
        for i in range(len(strs)):
            cd[tuple(sorted(strs[i]))] += i,

        res, items = [], cd.items()
        for item in items:
            res += [strs[i] for i in item[1]],
        return res
        

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams_2(["eat","tea","tan","ate","nat","bat"]))