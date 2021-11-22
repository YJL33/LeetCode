from typing import List
import bisect
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # lis?
        lis = []
        pairs.sort()
        for i in range(len(pairs)):
            p = pairs[i]
            if not lis or p[0] > lis[-1][1]:
                lis.append(p)
            else:
                i = bisect.bisect_left([b[-1] for b in lis], p[0])
                if p[1] <= lis[i][1]:
                    lis[i] = p
            # print('lis:', lis)
        return len(lis)

print(Solution().findLongestChain([[1,2],[2,3],[3,4]]))
print(Solution().findLongestChain([[1,2],[7,8],[4,5],[3,10]]))
print(Solution().findLongestChain([[1,2],[3,10],[7,8],[4,5]]))