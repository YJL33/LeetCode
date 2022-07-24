from typing import List
import collections
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 2 pass
        # check one side to impossible first, record all possible "removals" at that side
        # e.g. [3,2,20,1,1,3], check 10-3 => 10-3-2 => 10-3-2-20 (impossible)
        #                       record 3     record 5
        #      check 10-3       => 10-3-1       => 10-3-1-1
        #           7 not exist  6 not exist       5 exist: output answer
        #
        # tc: O(n)
        # sc: O(n) for worst scenario
        
        left = collections.defaultdict(int)         # key: removal, value: number of removes
        originalx, count = x, 0
        res = float('inf')
        for n in nums:
            if x-n < 0: break
            x, count = x-n, count+1
            if x == 0:
                res = min(res, count)
                break
            left[originalx-x] = count
        
        left[0] = 0
        # print('left', left)
        
        count, x = 0, originalx
        for n in nums[::-1]:
            if x-n < 0: break
            x, count = x-n, count+1
            if x in left:
                res = min(res, count+left[x])
        
        return res if res <= len(nums) else -1