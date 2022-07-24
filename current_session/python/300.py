from typing import List
import bisect
class Solution:
    # clarification
    # any duplications?
    # input validity?
    # upperbound/lowerbound of nums[i]?
    # restrictions of memory? timeout?
    #
    # ideas/algorithm
    # DP
    # dp[i] is the longest increasing subsequence, ending with i
    # tc: O(n^2)
    #
    # binary search
    # maintain the LIS, and insert all new arr[i] into LIS
    # tc: O(n) for all element, O(logn) to find the insert location
    #
    # carefully handle the duplicates
    #
    # test cases (use this to go through)
    # [9,5,2,6,6,4,7,9]:
    # 9 -> [9]
    # 5 -> [5]
    # 2 -> [2]
    # 6 -> [2,6]
    # 6 -> (2,6), bisect_right(lis, 6) = 2, bisect_left(lis, 6) = 1 => we want [2,6], use bisect_left
    # 4 -> [2,4,6]
    # 7 -> [2,4,6]
    # 9 -> [2,4,6,9]
    #
    # [3,3,3,3,3] -> length = 1
    
    def lengthOfLIS(self, nums: List[int]) -> int:

        def bs_left(x):
            nonlocal lis
            if not len(lis): return 0
            l, r = 0, len(lis)
            while l < r:
                mid = (l+r)//2
                if lis[mid] >= x:        # x at the left side. if as same as target: keep seek at left side for better insert location (bisect_left)
                    r = mid
                else:
                    l = mid+1
            return l

        lis = []
        for n in nums:
            # x = bisect.bisect_left(lis, n)
            x = bs_left(n)
            if not lis or x >= len(lis):
                lis.append(n)
            else:
                lis[x] = n
        
        return len(lis)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))