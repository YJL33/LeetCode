import collections
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_cnt = collections.Counter(corridor)
        # edge case
        if seat_cnt["S"] < 2 or seat_cnt["S"]%2 == 1: return 0
        if seat_cnt["S"] == 2: return 1
        seat_cnt = 0
        gap, res = 0, 1
        for _, c in enumerate(corridor):
            if c == "S": seat_cnt += 1
            if seat_cnt>=2 and seat_cnt%2 == 0:         # no matter this is "C" or "S"
                gap += 1
            elif c == "S" and seat_cnt>=2 and seat_cnt%2 == 1:       # after a "S", it should be here
                res = (res*gap)%1000000007
                gap = 0
            else:
                continue

        return res
