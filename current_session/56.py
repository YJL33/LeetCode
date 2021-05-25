"""
see https://leetcode.com/problems/merge-intervals/
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(nlogn) + O(n)
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            p, q = intervals[i]
            j = i+1
            while j < len(intervals) and intervals[j][0] <= q:
                q = max(intervals[j][1], q)
                j += 1
            res += [p, q],
            i = j
            # print i, j,res
        return res

print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
