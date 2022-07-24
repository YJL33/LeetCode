class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # there's only 2 interpretion since 100//60 == 1

        # calculate cost
        def calculate(mm, ss, pos):
            print('mm, ss', mm, ss)
            # for each digit, make sure its needed first, if needed, check if need to move, then add push cost
            cost = 0
            if mm != 0:
                m1, m2 = mm//10, mm%10
                if mm == 100:
                    m0 = 1
                    if m0 != pos:
                        cost += moveCost
                        pos = m0
                    cost += pushCost
                if m1 != 0:
                    if m1 != pos:
                        cost += moveCost
                        pos = m1
                    cost += pushCost
                if m2 != pos:
                    cost += moveCost
                cost += pushCost
                pos = m2
            print('cost m', cost)
            s1, s2 = ss//10, ss%10
            # when do we need s1?
            # a. s1 is not zero
            # b. s1 is zero, but mm is not zero
            if s1 != 0 or (s1 == 0 and mm != 0):
                if s1 != pos :
                    cost += moveCost
                    pos = s1
                cost += pushCost
            # s2 is definitely needed
            if s2 != pos:
                cost += moveCost
            cost += pushCost
            print('cost m+s', cost)
            return cost
        
        tm, ts = targetSeconds//60, targetSeconds%60
        c1 = calculate(tm, ts, startAt)
        
        if tm >= 1 and ts <= 39:
            tm2, ts2 = tm-1, ts+60
            return min(c1, calculate(tm2, ts2, startAt))
        else:
            return c1