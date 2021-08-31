from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # simply use binary Search
        def binarySearch(A):
            l, r = 0, len(A)-1
            while l < r:
                m = l + (r-l)//2
                if A[m-1]>=A[m] and A[m]<=A[-1]:
                    return A[m]
                elif A[m] > A[0]:
                    l = m+1
                elif A[m] < A[-1]:
                    r = m
                else:
                    print("???")
            # print('return l')
            return A[l]
        
        if len(nums) == 1: return nums[0]
        # elif len(nums) == 2: return min(nums)

        return binarySearch(nums) if nums[0] > nums[-1] else nums[0]

print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([11,13,15,17]))