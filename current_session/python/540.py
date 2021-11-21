from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # if all elements appeared twice
        # we should have a[i] == a[i+1] for all even i
        if len(nums)==1: return nums[0]

        l, r = 0, len(nums)-1

        def isTarget(arr, i):
            if i == 0:
                return arr[i] != arr[i+1]
            elif i == len(arr)-1:
                return arr[i] != arr[i-1]
            else:
                return arr[i] != arr[i+1] and arr[i] != arr[i-1]

        while l <= r:
            m = (l+r)//2
            if isTarget(nums, m):
                return nums[m]
            elif (m%2==1 and nums[m] == nums[m-1]) or (m%2==0 and nums[m] == nums[m+1]):
                l = m+1
            else:
                r = m-1
            # print('l, r', l, r)
        
        return -1

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))