"""
983
"""
import bisect
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # DP
        c1, c7, c30 = costs
        dp, res = [], float('inf')
        for i in range(len(days)):
            d, pc = days[i], 0
            if dp: 
                i = bisect.bisect_left([x[0] for x in dp], d)
                pc = min(x[-1] for x in dp[:i])
                dp = dp[i:]

            for day, cost in [(d,c1+pc),(d+6,c7+pc),(d+29,c30+pc)]:
                if day >= days[-1]:
                    res = min(res, cost)
                else:
                    bisect.insort_left(dp, (day,cost))
        return res


print(Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
print(Solution().mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]),'is 17')
print(Solution().mincostTickets([4,5,9,11,14,16,17,19,21,22,24],[1,4,18]), 'is 10')
print(Solution().mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29],[3,14,50]),'is 50')
