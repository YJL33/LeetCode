"""
 253. Meeting Rooms II

    Total Accepted: 25485
    Total Submissions: 67102
    Difficulty: Medium
    Contributors: Admin

Given an array of meeting time intervals: start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts, ends, num, endtime = [], [], 0, 0
        for i in intervals:
            starts += i.start,
            ends += i.end,

        starts.sort()
        ends.sort()
        
        for st in starts:
            if st < ends[endtime]: num += 1
            else: endtime += 1

        return num
