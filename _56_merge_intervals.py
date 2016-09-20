"""
56. Merge Intervals

    Total Accepted: 81699
    Total Submissions: 302593
    Difficulty: Hard

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # mergesort then combine intervals
        ans, i = [], 0

        intervals = self.sorter(intervals)

        while i < len(intervals):
            start, end, j = intervals[i].start, intervals[i].end, i+1
            while j < len(intervals) and intervals[j].start <= end:
                end = max(intervals[j].end, end)
                j += 1
            ans += Interval(start, end),
            i = j
        return ans

    def sorter(self, intervals):
        # implement mergesort
        if len(intervals) == 1:
            return [intervals[0]]
        elif len(intervals) > 1:
            mid = len(intervals)/2
            left, right = intervals[:mid], intervals[mid:]
            return self.merger(self.sorter(left), self.sorter(right))

    def merger(self, left, right):
        res, c1, c2 = [], 0, 0
        while c1 < len(left) and c2 < len(right):
            if left[c1].start < right[c2].start:
                res += left[c1],
                c1 += 1
            elif left[c1].start > right[c2].start:
                res += right[c2],
                c2 += 1
            else:
                if left[c1].end <= right[c2].end:
                    res += left[c1],
                    c1 += 1
                else:
                    res += right[c2],
                    c2 += 1

        if c1 == len(left):
            res += right[c2:]
        else:
            res += left[c1:]

        return res