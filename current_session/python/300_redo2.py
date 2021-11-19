from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # craft the LIS
        # maintain a lis and use binary search to insert the n
        # e.g. [2,5,3,4]
        # 2
        # 2 5 -> 2 3
        # 2 3 4
        def bs(arr, x):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] < x:       # target at the right side
                    l = m+1
                else:
                    r = m
            return l

        lis = []
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
            else:
                i = bs(lis, n)
                lis[i] = n
            # print('lis:', lis)
        return len(lis)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))