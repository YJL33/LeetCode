from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # use DP
        # dp[j] is the solution of intervals[:j]
        # where it keeps the last keeping interval index i_last, and numbers removed cnt
        # if int[i] is overlapped with int[i+1]
        # either remove this one or remove previous one (since the one before previous one won't overlap)
        # dp[i+1] = (i1, prev_cnt+1) or (i, prev_cnt+1)
        # if no overlap, simply add this one
        # print(intervals)

        # sort based on start time
        intervals.sort()

        dp = [[-1,0] for _ in range(len(intervals)+1)]
        dp[1] = [0,0]
        for i in range(2,len(intervals)+1):
            prev_i, prev_cnt = dp[i-1]
            si, ei = intervals[i-1]
            sp, ep = intervals[prev_i]
            # print('current', intervals[i-1])
            # print('previous', intervals[prev_i])
            if (sp < ei) and (si < ep):    # overlap
                if ep <= ei:
                    dp[i] = [prev_i, prev_cnt+1]        # remove current one
                else:
                    dp[i] = [i-1, prev_cnt+1]           # remove previous one
            else:
                dp[i] = [i-1, prev_cnt]
        # print(dp)
        return dp[-1][-1]

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # optimized (also DP)
        if len(intervals) == 1: return 0
        intervals.sort()
        prev_i, cnt = 0, 0
        for i in range(1,len(intervals)):
            si, ei = intervals[i]
            sp, ep = intervals[prev_i]
            if (sp < ei) and (si < ep):     # overlap
                if ep <= ei:
                    cnt = cnt+1             # remove current one
                else:
                    prev_i, cnt = i, cnt+1  # remove previous one
            else:
                prev_i = i
        return cnt

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: sort by end time and check each start time
        if len(intervals) == 1: return 0
        intervals.sort(key = lambda x: x[1])
        end, cnt = float('-inf'), 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
            
print(Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]), '== 7')
