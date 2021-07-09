"""
see https://leetcode.com/problems/insert-interval/
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        toMerge = []
        before, after = [], []
        for i in intervals:
            s, e = i[0], i[1]
            if e < newInterval[0]:
                before += i,
            elif s > newInterval[1]:
                after += i,
            else:
                toMerge += i,

        ns, ne = newInterval[0], newInterval[1]
        for x in toMerge:
            ns = min(x[0], ns)
            ne = max(x[1], ne)

        return before + [[ns, ne]] + after

print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
