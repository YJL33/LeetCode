class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num = target
        d_cnt = 0
        inc_cnt = 0
        while num != 1:
            if num % 2 == 0 and d_cnt < maxDoubles:
                num = num//2
                d_cnt += 1
            else:
                if d_cnt < maxDoubles:
                    num -= 1
                    inc_cnt += 1
                else:
                    inc_cnt += (num-1)
                    num = 1
        return d_cnt+inc_cnt


print(Solution().minMoves(766972377,92))
