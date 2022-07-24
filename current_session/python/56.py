"""
see https://leetcode.com/problems/merge-intervals/
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # clarification:
        # any restriction on memory? time complexity?
        # is the intervals sorted?
        # [1,4)? or [1,4]?
        # is all given intervals valid? (e.g. negitives?)
        # upperbound, lowerbound of intervals[i], intervals[j]?? 0-10^4
        # size of given intervals = 1-10^4
        
        # naive approach (brute force):
        # simply try all possible i, j for 0<=i,j<len(intervals) and merge if there's overlap
        # like union find, treating each interval as node in a graph, and need to check all 'edges' if exist
        # time complexity O(N^2)
        
        # use two pointer
        # sort the intervals first (by starttime), we have first element (t1, x), where starttime = t1, endtime = x
        # go through the array (from earlier starttime), merge all intervals(a,b) has starttime <= x, and update x = max(x, b)
        # until we have starttime > x, add (t1, x) to the result, so on and so forth
        # time analysis: 
        # timsort avg case O(NlogN)/worst case O(NlogN)/best case O(N)
        # go through the array O(N)
        # overall: O(NlogN)+O(N)
        # space analysis:
        # timsort O(N)
        # two pointers O(1)
        # overall: O(N)+O(1)
        
        # test case walk through
        
        N = len(intervals)
        intervals.sort()
        start_time, end_time = intervals[0]
        
        res = []
        for i in range(1,N):
            if intervals[i][0] <= end_time:
                end_time = max(end_time, intervals[i][1])
            else:
                res.append([start_time, end_time])
                start_time, end_time = intervals[i]
        
        res.append([start_time, end_time])
        return res

print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
