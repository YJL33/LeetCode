"""
435. Non-overlapping Intervals

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Given a collection of intervals,
find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Example 1:

Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [ [1,2], [2,3] ]

Output: 0

Explanation:
You don't need to remove any of the intervals since they're already non-overlapping.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start, end = [], []
        for i in intervals:
            start += (i.start, i),
            end += (i.end, i),

        start.sort(reverse=True)
        end.sort(reverse=True)

        cur = start.pop()
        current = [cur[1]]

        while start or end:
            if start[-1][0] <= end[-1][0]:
                next = start.pop()
                current += next,
                cur = next[0]
            else:
                current

        