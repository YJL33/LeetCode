from typing import List
import bisect
import collections
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # keep update LIS and count while updating
        # e.g. [1,3,5,7,2,4,6,8]
        # lis [1] [1,3] [1,3,5] [1,3,5,7]
        # lis [1] [1,3][1,2] [1,3,5] [1,3,5,7]
        # lis [1] [1,3][1,2] [1,3,5][1,3,4][1,2,4] [1,3,5,7]
        # lis [1] [1,3][1,2] [1,3,5][1,3,4][1,2,4] [1,3,5,7][1,3,5,6][1,3,4,6][1,2,4,6]
        # lis [1] [1,3][1,2] [1,3,5][1,3,4][1,2,4] [1,3,5,7][1,3,5,6][1,3,4,6][1,2,4,6] ...
        lis = []
        cnt = []        # a counter with key=lis element
        for i in range(len(nums)):
            n = nums[i]
            if not lis or n > lis[-1]:
                lis.append(n)
                x = collections.defaultdict(int)
                x[n] = 1 if not cnt else sum([v for k, v in cnt[-1].items() if k < n])
                cnt.append(x)
            else:
                i = bisect.bisect_left(lis, n)
                lis[i] = n
                cnt[i][n] += 1 if i-1 < 0 else sum([v for k, v in cnt[i-1].items() if k < n])
            # print('lis:',lis)
            # print('cnt:',cnt)
        return sum(cnt[-1].values())

# print(Solution().findNumberOfLIS([1,3,5,4,7]))
# print(Solution().findNumberOfLIS([2,2,2,2,2]))
print(Solution().findNumberOfLIS([1,3,5,7,6,4,2,1,3,5,7]))
# print(Solution().findNumberOfLIS([1,3,5,4,7,2,5,7,3,5,7,9,1,4,6,2,4,5,6,7,8,2,3,4,5,6,7,8,2,3,4,5,6,7,3,4,5,6,7,8]))