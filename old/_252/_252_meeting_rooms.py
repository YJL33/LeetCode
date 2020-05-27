"""
252. Meeting Rooms

    Total Accepted: 16823
    Total Submissions: 38196
    Difficulty: Easy

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        meetings = []
        for i in intervals:
            meetings += [i.start, i.end],
        meetings.sort()
        for i in xrange(len(meetings)-1):
            if meetings[i][1] > meetings[i+1][0]:
                return False
        return True