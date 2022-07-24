from functools import lru_cache

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # mathematically way:
        # only count the tail, and add next possible number into counts
        # can not use due to distinct rule

        # we need to check whether 'skip' value is there
        # we can keep use 'layers'
        
        skip = {(1,7):4,(1,3):2,(1,9):5,(2,8):5,(3,7):5,(3,9):6,(4,6):5,(7,9):8}

        @lru_cache(None)
        def dp(i):
            if i == 1: return [[x] for x in range(1,10)]
            prev = dp(i-1)
            tmp = []
            for p in prev:
                for a in range(1,10):
                    if a not in p:
                        tail = p[-1]
                        edge = (min(a, tail), max(a, tail))
                        if edge not in skip or skip[edge] in p:
                            tmp.append(p+[a])
            return tmp

        count = 0
        for i in range(m, n+1):
            count += len(dp(i))
        
        return count

print(Solution().numberOfPatterns(1,1))
print(Solution().numberOfPatterns(1,2))