from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort it first (based on x-end or x-start?)
        # very similar to meeting rooms problem
        points.sort()
        # print('points:', points)
        cnt = 1
        prev_arrow = (points[0][0], points[0][1])
        for s, e in points:
            ps, pe = prev_arrow
            if s <= ps <= e or s <= pe <= e or ps <= s <= pe or ps <= e <= pe:
                prev_arrow = (max(ps, s), min(pe, e))
                continue
            else:
                # print('p:', s, e)
                cnt += 1
                prev_arrow = (s,e)
        return cnt

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
