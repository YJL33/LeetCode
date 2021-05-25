"""
https://leetcode.com/problems/interval-list-intersections/
"""
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # change A and B into series of 'start' and 'end' events
        events = []
        for a in A:
            events += (a[0], 'b'),
            events += (a[1], 'e'),
        for b in B:
            events += (b[0], 'b'),
            events += (b[1], 'e'),
        events.sort()

        # optimization: use 2 cursors and get rid of the above part
        res, cntOfIntvl, s = [], 0, None
        for i in range(len(events)):
            if events[i][1] == 'b':
                cntOfIntvl += 1
                if cntOfIntvl == 2:
                    s = events[i][0]
            else:
                cntOfIntvl -= 1
                if cntOfIntvl == 1:
                    res += [s, events[i][0]],

        # print res
        return res

print(Solution().intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))

