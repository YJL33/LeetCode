from typing import List
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # clarification:
        # can we rotate?
        # fit in criteria
        #
        # thoughts:
        # DP
        # rotate all boxes first s.t. we have w <= l <= h
        # sort all the rotate boxes by width (or l, h, any should be good?)
        #
        # dp[i+1] is the max_total_height (status), while using boxes[:i]
        #
        # we can keep 2 values here: (a) WITH boxes[i] and (b) WITHOUT boxes[i]
        # however, it seems to be necessary to check all j < i to find out (a)
        #
        # THEREFORE:
        # dp[i+1] is the max_total_height WITH boxes[i], while using boxes[:i]
        #
        # for each box i, check all previous j
        # if we have wj <= wi and lj <= li and hj <= hi: dp[i] = max(dp[i], dp[j]+hi)
        # 
        # return max(dp)
        #
        # test cases: [[50,45,20],[95,37,53],[21,40,40],[45,23,12]]
        #           ->[[12,23,45],[20,45,50],[21,40,40],[37,53,95]]
        #           ->        45         95         40        190
        #
        # analysis
        # tc: O(n^2)
        # sc: O(n)

        cuboids = [[0,0,0]] + sorted(map(sorted, cuboids))
        dp = [0 for _ in range(len(cuboids))]
        for i in range(1, len(cuboids)):
            for j in range(i):
                if all(cuboids[j][k] <= cuboids[i][k] for k in range(3)):
                    dp[i] = max(dp[i], dp[j]+cuboids[i][2])
        return max(dp)